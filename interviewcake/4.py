

def condense_meeting_times(mtg_list):
    """ takes a list of meeting time ranges
    and returns a list of condensed ranges """

    # u know mtg overlaps if 2nd start time > 1st end time of prev
    # 1st end time > start time of second
    busy_times = []
    
    # sort by start time
    sorted_mtgs = sorted(mtg_list)

    # initialize merged_meetings with the earliest
    merged_meetings = [sorted_mtgs[0]]

    for current_meeting_start, current_meeting_ed in sorted_mtgs[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        # if the curr and last meeting overlaps, use the latest end time
        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))



mtg_list = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
condense_meeting_times(mtg_list)