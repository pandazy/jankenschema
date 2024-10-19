import json
from .utils import snake_to_camel
from .db_column import DbColumn
from .gen_common import TYPE_MAP


TS_TEMPLATE = """
/**
 * This file was generated by the extract tool.
 * Do not modify this file manually.
 * 
 */

/**
 * The type of string constrained to the field names of the %(table_entity)s
 */
export type FieldNameType = %(field_type_list)s;


/**
 * The entity type of the %(table_entity)s
 */
export interface %(table_entity)s {
%(field_defs)s
}

/**
 * The data-column names list of the %(table_entity)s
 */
export const FIELD_NAMES: readonly FieldNameType[] = Object.freeze([%(field_names)s]);

/**
 * The source-of-truth resource name resource name (database table name) of the %(table_entity)s
 */
export const RESOURCE_NAME = '%(resource_name)s';

%(const_table_names)s

/**
 * The data-column name set of the %(table_entity)s
 */
export const FieldNameSet: ReadonlySet<FieldNameType> = Object.freeze(new Set(FIELD_NAMES));

/**
 * Create a new %(table_entity)s with the default values set if not provided
 */
export function build(input: %(table_entity)s): %(table_entity)s {
    const ret = {} as Record<FieldNameType, any>;
%(set_default_vals)s
    return ret;
}
"""


def get_ts_code(resource_name: str, column_defs: list[DbColumn]) -> str:
    """
    Generate TypeScript code for a database table schema

    :param resource_name: The name of the database table
    :param column_defs: The list of column definitions
    """
    field_defs = []
    field_names = []
    const_table_names = []
    set_default_vals = []
    for col in column_defs:
        required = "" if col.not_null else "?"
        field_defs.append(f"\t{col.name}{required}: {TYPE_MAP[col.field_type]['ts']};")
        field_names.append(f"'{col.name}'")
        const_table_names.append(
            f'export const COL_NAME_{col.name.upper()} = "{col.name}";'
        )
        if col.default_val is not None:
            display_val = (
                col.default_val
                if col.field_type != "TEXT"
                else f"{json.dumps(col.default_val)}"
            )
            set_default_vals.append(
                f"\t\tret.{col.name} = input.{col.name} == null ? {display_val} : input.{col.name}; // use `==null` to check for null or undefined"
            )

    return TS_TEMPLATE % {
        "table_entity": snake_to_camel(resource_name, True),
        "field_defs": "\n".join(field_defs),
        "field_names": ", ".join(field_names),
        "field_type_list": " | ".join(field_names),
        "resource_name": resource_name,
        "set_default_vals": "\n".join(set_default_vals),
        "const_table_names": "\n".join(const_table_names),
    }
