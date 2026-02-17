def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''

    global cur_hedons, cur_health

    global cur_time
    global last_activity, last_activity_duration

    global last_finished
    global bored_with_stars

    cur_hedons = 0
    cur_health = 0

    cur_star = None
    cur_star_activity = None

    bored_with_stars = False

    last_activity = None
    last_activity_duration = 0

    cur_time = 0

    last_finished = -1000

    global running_duration
    running_duration = 0

    global star_running
    star_running = False

    global star_textbook
    star_textbook = False

    global last_star_time
    global second_last_star_time

    last_star_time = -120
    second_last_star_time = -120


def star_can_be_taken(activity):
    pass


def perform_activity(activity, duration):
    global cur_hedons, cur_health, running_duration, cur_time, last_finished, star_running, star_textbook

    if activity == "running":
        # Update health
        if running_duration >= 180:
            cur_health = cur_health + duration * 1
        elif running_duration + duration >= 180:
            cur_health = cur_health + (180 - running_duration) * 3 + (running_duration + duration - 180) * 1
        else:
            cur_health = cur_health + duration * 3

        # Update hedons (for tired)
        if (cur_time - last_finished) < 120:
            cur_hedons = cur_hedons - duration * 2
        else:
            if duration > 10:
                cur_hedons = cur_hedons + 10 * 2 - (duration - 10) * 2
            else:
                cur_hedons = cur_hedons + duration * 2

        # Update hedons (for star)
        if star_running:
            if duration > 10:
                cur_hedons = cur_hedons + 30
            else:
                cur_hedons = cur_hedons + duration * 3

            star_running = False

        # Update running duration
        running_duration = running_duration + duration

        # Update last time
        last_finished = cur_time + duration
        # print("last_finished: ", last_finished)

    elif activity == "textbooks":
        # Update health
        cur_health = cur_health + duration * 2

        # Update hedons (for tired)
        if (cur_time - last_finished) < 120:
            cur_hedons = cur_hedons - duration*2
        else:
            if duration > 20:
                cur_hedons = cur_hedons + 20 * 1 - (duration - 20) * 1
            else:
                cur_hedons = cur_hedons + duration

        # Update hedons (for star)
        if star_textbook:
            if duration > 10:
                cur_hedons = cur_hedons + 30
            else:
                cur_hedons = cur_hedons + duration * 3

            star_textbook = False

        # Update running duration
        running_duration = 0

        # Update last time
        last_finished = cur_time + duration

    elif activity == "resting":
        cur_health = cur_health + 0
        cur_hedons = cur_hedons + 0

        # Update running duration
        running_duration = 0

    else:
        return

    # Update time
    cur_time = cur_time + duration


def get_cur_hedons():
    return cur_hedons


def get_cur_health():
    return cur_health


def offer_star(activity):
    global star_textbook, star_running
    global last_star_time, second_last_star_time, cur_time

    second_last_star_time = last_star_time
    last_star_time = cur_time

    if cur_time - second_last_star_time < 120:
        return

    if activity == "textbooks":
        star_textbook = True
    elif activity == "running":
        star_running = True
    else:
        return


def most_fun_activity_minute():
    global cur_hedons, cur_health, cur_time, last_finished, running_duration, star_running, star_textbook
    global last_activity, last_activity_duration, bored_with_stars

    # Remember initial value
    cur_hedons_before = cur_hedons
    cur_health_before = cur_health
    cur_time_before = cur_time
    last_finished_before = last_finished
    running_duration_before = running_duration
    star_running_before = star_running
    star_textbook_before = star_textbook
    last_activity_before = last_activity
    last_activity_duration_before = last_activity_duration
    bored_with_stars_before = bored_with_stars

   
