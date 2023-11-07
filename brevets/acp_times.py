"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    # Define the maximum speeds based on brevet distance
    if control_dist_km <= 200:
        max_speed_kmh = 34
    elif 200 < control_dist_km <= 300:
        max_speed_kmh = 32
    elif 300 < control_dist_km <= 400:
        max_speed_kmh = 32
    elif 400 < control_dist_km <= 600:
        max_speed_kmh = 30
    elif 600 < control_dist_km < 1000:
        max_speed_kmh = 28
    elif control_dist_km == 1000:
        max_speed_kmh = 26

    # Calculate the time it takes to reach the control point
    time_hour = control_dist_km / max_speed_kmh

    time_min = (time_hour*60) + .5

    int(time_min)

    # Calculate the open time based on the brevet start time
    open_time_calc = brevet_start_time.shift(minutes=time_min)

    return open_time_calc

def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    if control_dist_km == 0:
        close_time_calc = brevet_start_time.shift(hours=1)
        return close_time_calc
    else:
        # Define the minimum speeds based on brevet distance
        if control_dist_km <= 200:
            min_speed_kmh = 15
        elif 200 < control_dist_km <= 300:
            min_speed_kmh = 15
        elif 300 < control_dist_km <= 400:
            min_speed_kmh = 15
        elif 400 < control_dist_km <= 600:
            min_speed_kmh = 15
        elif 600 < control_dist_km < 1000:
            min_speed_kmh = 11.428
        elif control_dist_km == 1000:
            min_speed_kmh = 13.333

        if brevet_dist_km == 200 and control_dist_km == 200:
            # Calculate the time it takes to reach the control point
            time_hour = control_dist_km / min_speed_kmh

            time_min = (time_hour*60) + .5

            int(time_min)

            # Calculate the open time based on the brevet start time
            close_time_calc = brevet_start_time.shift(minutes=time_min+10)

            return close_time_calc
        
        elif brevet_dist_km == 400 and control_dist_km == 400:
            # Calculate the time it takes to reach the control point
            time_hour = control_dist_km / min_speed_kmh

            time_min = (time_hour*60) + .5

            int(time_min)

            # Calculate the open time based on the brevet start time
            close_time_calc = brevet_start_time.shift(minutes=time_min+20)

            return close_time_calc

        else:
            # Calculate the time it takes to reach the control point
            time_hour = control_dist_km / min_speed_kmh

            time_min = (time_hour*60) + .5

            int(time_min)

            # Calculate the open time based on the brevet start time
            close_time_calc = brevet_start_time.shift(minutes=time_min)

            return close_time_calc

