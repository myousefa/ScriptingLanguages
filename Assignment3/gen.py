import re
import argparse

def main():
    # ------------------------------------ PART ONE --------------------------------------- #
    # Understanding cmd line arguement
    parser = argparse.ArgumentParser()
    parser.add_argument("base_file")
    parser.add_argument("comparison_file")
    args = parser.parse_args()

    # ----------------------------- FIELDS ------------------------------- #
    # Container for adding info in .log files into maps
    base_CookieMap = {}
    base_SegMap = {}
    comparison_CookieMap = {}
    comparison_SegMap = {}

    # Container for segments to cookies and cookies to segments 
    segment_Added = {}
    segment_Missing = {}
    cookie_Added = {} 
    cookie_Missing = {}
    # -------------------------------------------------------------------- #

    # Generating map for summary information
    gen_cookie_seg_map(args.base_file, base_CookieMap, base_SegMap)
    gen_cookie_seg_map(args.comparison_file, comparison_CookieMap, comparison_SegMap)

    # Print rundown/summary of now built maps
    print_rundown(base_CookieMap, comparison_CookieMap)

    # ---------------------------------- PART ONE DONE ------------------------------------ #
    

    # ------------------------------------ PART TWO --------------------------------------- #
    # Generate seg map and cookie map and check for added and missing cookies and extra segments and omitted segments
    gen_uniq_map(base_SegMap, comparison_SegMap, segment_Added, segment_Missing)
    gen_uniq_map(base_CookieMap, comparison_CookieMap, cookie_Added, cookie_Missing)

    # ------------------------- FINAL REPORT ----------------------------- #
    # Print map contents
    print("Segments with added cookies:", len(segment_Added.keys()), "/", len(base_SegMap.keys()))
    final_report(segment_Added)
    print()

    print("Segments with missing cookies:", len(segment_Missing.keys()), "/", len(base_SegMap.keys()))
    final_report(segment_Missing)
    print()

    print("Cookies in extra segments:", len(cookie_Added.keys()), "/", len(base_CookieMap.keys()))
    final_report(cookie_Added)
    print()

    print("Cookies omitted from segments:", len(cookie_Missing.keys()), "/", len(base_CookieMap.keys()))
    final_report(cookie_Missing)
    print()
    # ------------------------- FINAL REPORT ----------------------------- #
    # ---------------------------------- PART TWO DONE ------------------------------------ #

def gen_cookie_seg_map(filename, cookie_map, seg_map):
    with open(filename) as f:
        for line in f:
            # regex expression and using built in python function to match 
            regexmatch = re.match(r"\d+:\d+:\d+.\d+ \[main\] ERROR com.audiencescience.app.smac(\d)?.functional.EvaluateProfiles - evaluated:", line)
            if (regexmatch):
                # use regex to find all cookies and segments and append into map
                cookie = re.search(r"\w{32}", line).group(0)
                segments = set(re.findall(r"([A-Z]+\d+_\d+)", line))                
                cookie_map[cookie] = segments
                for seg in segments:
                    if seg in seg_map:
                        seg_map[seg].add(cookie)
                    else:
                        seg_map[seg] = { cookie }
    
def gen_uniq_map(baseMap, comparisonMap, addedMap, missingMap):
    for key in baseMap:
        if key not in comparisonMap:
            comparisonMap[key] = set()
        if (baseMap[key] and not comparisonMap[key]):
            if (comparisonMap[key] - baseMap[key]):
                addedMap[key] = comparisonMap[key] - baseMap[key]
            else: 
                missingMap[key] = baseMap[key] - comparisonMap[key]

def print_rundown(base_map, comparison_map):
    base_cookies = set(base_map.keys())
    base_empty_cookies = { i for i in base_map if not base_map[i] } 
    baseline_nonempty_cookies = base_cookies - base_empty_cookies

    comparison_cookies = set(comparison_map.keys())
    comparison_empty_cookies = { i for i in comparison_map if not comparison_map[i] } 
    comparison_nonempty_cookies = comparison_cookies - comparison_empty_cookies

    # Printing Rundown/Summary
    print("Summary:")
    print("total cookies in baseline = ", len(base_cookies))
    print("empty cookies in baseline = ", len(base_empty_cookies))
    print("non-empty cookies in baseline = ", len(base_cookies) - len(base_empty_cookies))
    print("total cookies in test = ", len(comparison_cookies))
    print("empty cookies in test = ", len(comparison_empty_cookies))
    print("non-empty cookies in test = ", len(comparison_cookies) - len(comparison_empty_cookies))
    print("non-empty cookies in baseline only = ", len(baseline_nonempty_cookies ))
    print("non-empty cookies in test only = ", len(comparison_nonempty_cookies))
    print("non-empty cookies in both = ", len(baseline_nonempty_cookies & comparison_nonempty_cookies))
    print("non-empty cookies in either = ", len(baseline_nonempty_cookies | comparison_nonempty_cookies))
    print()


def final_report(map):
    for index, key in enumerate(sorted(map)):
        err = list(map[key])
        print(index, key, len(err), err,  sep= '\t')

if __name__ == "__main__":
    main()