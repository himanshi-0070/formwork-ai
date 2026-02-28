import math

def schedule_based_reuse(total_quantity, reuse_limit, project_duration_days, cycle_time_days):

    max_cycles_per_mould = project_duration_days // cycle_time_days

    effective_capacity = reuse_limit * max_cycles_per_mould

    moulds_required = math.ceil(total_quantity / effective_capacity)

    return moulds_required, effective_capacity
