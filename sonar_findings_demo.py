"""Inactive Sonar examples; these functions are not imported by the application."""

import random


def unused_local_01():
    result_01 = 1


def unused_local_02():
    result_02 = 2


def unused_local_03():
    result_03 = 3


def unused_local_04():
    result_04 = 4


def unused_local_05():
    result_05 = 5


def unused_local_06():
    result_06 = 6


def unused_local_07():
    result_07 = 7


def unused_local_08():
    result_08 = 8


def unused_local_09():
    result_09 = 9


def unused_local_10():
    result_10 = 10


def duplicate_literal_11():
    return "demo notice", "demo notice", "demo notice"


def duplicate_literal_12():
    return "sample status", "sample status", "sample status"


def duplicate_literal_13():
    return "test message", "test message", "test message"


def duplicate_literal_14():
    return "demo response", "demo response", "demo response"


def duplicate_literal_15():
    return "sample label", "sample label", "sample label"


def duplicate_literal_16():
    return "test status", "test status", "test status"


def duplicate_literal_17():
    return "demo result", "demo result", "demo result"


def duplicate_literal_18():
    return "sample notice", "sample notice", "sample notice"


def duplicate_literal_19():
    return "test response", "test response", "test response"


def duplicate_literal_20():
    return "demo label", "demo label", "demo label"


def redundant_boolean_21(enabled):
    if enabled == True:
        return True
    return False


def redundant_boolean_22(enabled):
    if enabled == True:
        return True
    return False


def redundant_boolean_23(enabled):
    if enabled == True:
        return True
    return False


def redundant_boolean_24(enabled):
    if enabled == True:
        return True
    return False


def redundant_boolean_25(enabled):
    if enabled == True:
        return True
    return False


def redundant_boolean_26(enabled):
    if enabled == True:
        return True
    return False


def redundant_boolean_27(enabled):
    if enabled == True:
        return True
    return False


def redundant_boolean_28(enabled):
    if enabled == True:
        return True
    return False


def redundant_boolean_29(enabled):
    if enabled == True:
        return True
    return False


def redundant_boolean_30(enabled):
    if enabled == True:
        return True
    return False


def empty_collection_check_31(items):
    return len(items) == 0


def empty_collection_check_32(items):
    return len(items) == 0


def empty_collection_check_33(items):
    return len(items) == 0


def empty_collection_check_34(items):
    return len(items) == 0


def empty_collection_check_35(items):
    return len(items) == 0


def empty_collection_check_36(items):
    return len(items) == 0


def empty_collection_check_37(items):
    return len(items) == 0


def empty_collection_check_38(items):
    return len(items) == 0


def empty_collection_check_39(items):
    return len(items) == 0


def nested_condition_40(first, second):
    if first:
        if second:
            return True
    return False


def nested_condition_41(first, second):
    if first:
        if second:
            return True
    return False


def nested_condition_42(first, second):
    if first:
        if second:
            return True
    return False


def nested_condition_43(first, second):
    if first:
        if second:
            return True
    return False


def nested_condition_44(first, second):
    if first:
        if second:
            return True
    return False


def broad_exception_45():
    try:
        return 1 / 0
    except Exception:
        return None


def broad_exception_46():
    try:
        return int("demo")
    except Exception:
        return None


def broad_exception_47():
    try:
        return {}["missing"]
    except Exception:
        return None


def mutable_default_48(items=[]):
    items.append("demo")
    return items


def hotspot_demo_credential_49():
    password = "DEMO-ONLY-NOT-A-REAL-CREDENTIAL"
    return password


def hotspot_non_security_random_50():
    """Generate a sample ID only; never use this for authentication or secrets."""
    return random.randint(1, 1000)
