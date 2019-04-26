# Thanks to https://steamcommunity.com/app/363890/discussions/0/490125103619538453/
#
# Base Value <10;50> - base value for calculating necessary EXP
# Extra Value <0;40> - a simple extra value added to the EXP necessary for each level
# Acceleration A <10;50> - a value representing the rate at which to increase the necessary EXP. Affects the entire EXP curve.
# Acceleration B <10;50> - a value representing the degree at which to exponentially increase the necessary EXP. Mainly affects the high-level range.

def _total_exp_for_level(level, base_value=30, extra_value=20, acceleration_A=30, acceleration_B=30):
    return round(base_value*(pow(level-1, 0.9+acceleration_A/250))*level*(level+1)/(6+pow(level,2)/50/acceleration_B)+(level-1)*extra_value)

def _exp_to_level(level_curr, level_dest, base_value=30, extra_value=20, acceleration_A=30, acceleration_B=30):
    return _total_exp_for_level(level_dest, base_value, extra_value, acceleration_A, acceleration_B) - expForLevel(level_curr, base_value, extra_value, acceleration_A, acceleration_B)

def _total():
    print("Total exp:")
    for x in range(1,100):
        print("{0}: {1}".format(x, _total_exp_for_level(x)))

def _next_level():
    print("Exp for next level:")
    for x in range(1, 100):
        print("{0}: {1}".format(x, _exp_to_level(x, x+1)))

def get_total_exp_list(from_=1, to_=99, base_value=30, extra_value=20, acceleration_A=30, acceleration_B=30):
    return [_total_exp_for_level(x, base_value, extra_value, acceleration_A, acceleration_B) for x in range(from_, to_+1)]

def get_exp_for_next_level_list(from_=1, to_=99, base_value=30, extra_value=20, acceleration_A=30, acceleration_B=30):
    exp_list = get_total_exp_list(from_, to_+1, base_value, extra_value, acceleration_A, acceleration_B)

    return [exp_list[x+1]-exp_list[x] for x in range(len(exp_list)-1)]

# Usage examples:
#
# x = get_total_exp_list(1,32)
# y = get_exp_for_next_level_list(1,32)