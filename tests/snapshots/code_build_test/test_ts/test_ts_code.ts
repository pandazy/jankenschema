
/**
 * This file was generated by the extract tool.
 * Do not modify this file manually.
 * 
 */

/**
 * The type of string constrained to the field names of the TsTestTable
 */
export type FieldNameType = 'id' | 'name' | 'age' | 'cash' | 'dep';


/**
 * The entity type of the TsTestTable
 */
export interface TsTestTable {
	id: number;
	name: string;
	age?: number;
	cash?: number;
	dep?: string;
}

/**
 * The data-column names list of the TsTestTable
 */
export const FIELD_NAMES: readonly FieldNameType[] = Object.freeze(['id', 'name', 'age', 'cash', 'dep']);

/**
 * The source-of-truth resource name resource name (database table name) of the TsTestTable
 */
export const RESOURCE_NAME = 'ts_test_table';

export const COL_NAME_ID = "id";
export const COL_NAME_NAME = "name";
export const COL_NAME_AGE = "age";
export const COL_NAME_CASH = "cash";
export const COL_NAME_DEP = "dep";

/**
 * The data-column name set of the TsTestTable
 */
export const FieldNameSet: ReadonlySet<FieldNameType> = Object.freeze(new Set(FIELD_NAMES));

/**
 * Create a new TsTestTable with the default values set if not provided
 */
export function build(input: TsTestTable): TsTestTable {
    const ret = {} as Record<FieldNameType, any>;
		ret.age = input.age == null ? 9 : input.age; // use `==null` to check for null or undefined
		ret.cash = input.cash == null ? 4.2 : input.cash; // use `==null` to check for null or undefined
		ret.dep = input.dep == null ? "dev-\"big\"'BIG'" : input.dep; // use `==null` to check for null or undefined
    return ret;
}
