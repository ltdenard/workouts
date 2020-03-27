#!/usr/bin/env python3
import math
import argparse

def roundfive(x, base=5):
	""" No body has 0.1 lb weights. So we round to nearest 5."""
	return int(base * round(float(x)/base))

def normalize_length(s, slength=25):
	""" function to make workout table look right """
	slen = len(s)
	add_spaces = slength - slen
	for _ in range(0,add_spaces):
		s+=" "
	return s

# define exercise here
# first key is the number of exercises in a week
# value of that number if exercise name and the max
# EDIT THIS:
# this should be edited to the workouts you want 
# to do and your one-rep max
workout_lifts = {
	1:{
		"barbell_bench_press":180,
		"incline_barbell_bench": 130,
		"dumbbell_bench_press": 30,
		"seated_tricips_press": 30,
	},
	2:{
		"barbell_deadlift":160,
		"one_arm_dumbbell_rows":35,
		"dumbbell_reverse_incline":30,
		"barbell_curls":35,
		"calf_raises":35,
	},
	3:{
		"barbell_squat": 45,
		"front_squat":205,
		"dumbbell_romanian_deadlift":30,
		"seated_calf_raise":45
	}
}

# 12 weeks program defined.
# this is the reps and percentages for each week.
week_rep_percentages_dict = {
	1:{
		1:{
			3:0.82
		},
		2:{
			3:0.86
		},
		3:{
			3:0.91
		}
	},
	2:{
		1:{
			5:0.70
		},
		2:{
			5:0.74
		},
		3:{
			5:0.78
		},
		4:{
			5:0.82
		},
		5:{
			5:0.86
		}
	},
	3:{
		1:{
			5:0.84
		},
		2:{
			3:0.89
		},
		3:{
			1:0.94
		}
	},
	4:{
		1:{
			10:0.72
		},
		2:{
			8:0.76
		},
		3:{
			6:0.80
		}
	},
	5:{
		1:{
			3:0.84
		},
		2:{
			3:0.88
		},
		3:{
			3:0.93
		}
	},
	6:{
		1:{
			5:0.74
		},
		2:{
			5:0.76
		},
		3:{
			5:0.80
		},
		4:{
			5:0.84
		},
		5:{
			5:0.88
		}
	},
	7:{
		1:{
			5:0.87
		},
		2:{
			3:0.94
		},
		3:{
			1:1
		}
	},
	8:{
		1:{
			10:0.75
		},
		2:{
			8:0.79
		},
		3:{
			6:0.83
		}
	},
	9:{
		1:{
			3:0.86
		},
		2:{
			3:0.9
		},
		3:{
			3:0.94
		}
	},
	10:{
		1:{
			5:0.74
		},
		2:{
			5:0.78
		},
		3:{
			5:0.82
		},
		4:{
			5:0.86
		},
		5:{
			5:0.9
		}
	},
	11:{
		1:{
			5:0.89
		},
		2:{
			3:0.96
		},
		3:{
			1:1
		}
	},
	12:{
		1:{
			10:0.78
		},
		2:{
			8:0.82
		},
		3:{
			6:0.86
		}
	}
}


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-w", "--week", help="week number you're on.", type=int, required=True)
	parser.add_argument("-n", "--count", help="workout count number of the week", type=int, required=True)
	args = parser.parse_args()
	week_num = args.week
	workout_count = args.count
	workout_percentages = week_rep_percentages_dict.get(week_num)
	workouts = workout_lifts.get(workout_count)
	workout_table = []
	for workout_name,workout_max in workouts.items():
		normalized_title = normalize_length(workout_name)
		workout_title = "| {} |".format(normalized_title)
		tmp_list = [workout_title]
		for k,rep_dict in workout_percentages.items():
			for rep_count,rep_percent in rep_dict.items():
				weight = workout_max*rep_percent
				rweight = roundfive(weight)
				workout_lbs = "{}x{}lb".format(rep_count,rweight)
				normal_workout = normalize_length(workout_lbs, slength=8)
				workout_string = " {} |".format(normal_workout)
				tmp_list.append(workout_string)
		workout_complete_line = "".join(tmp_list)
		workout_table.append(workout_complete_line)

	max_line_length = max([len(w) for w in workout_table])
	separator = "".join(["-" for _ in range(0,max_line_length)])
	workout_table_data = "\n{}\n".format(separator).join(workout_table)
	complete_workout_table = "{}\n{}\n{}".format(separator,workout_table_data,separator)
	print(complete_workout_table)


if __name__ == '__main__':
	main()