import sys

def get_data(data):
    """
    Read in the data from stdin and 
    parse the key information and put it in the 
    data arrays
    """
    cookies = []
    segments = []
    for line in data:
        cookie = line.split("evaluated: ")[1].split(" ==>")[0]
        segment_data = line.split("==> ")[1].split(", ")
        segment_data[0] = segment_data[0].split('[')[1]
        segment_data[-1] = segment_data[-1].split(']')[0]

        cookies.append(cookie)
        segments.append(segment_data)
    return cookies,segments

def find_cookies(segments2find=[],cookies=None,segments=None):
    cookie_idxs = []
    if(len(segments2find) > 0):
        # Find the cookies that share all the segments that are in segments2find
        for idx,segment_lib in enumerate(segments):
            if(len(segment_lib) > 1):
                if( all( seg in segment_lib for seg in segments2find) ):
                    cookie_idxs.append(idx)
        return [cookies[idx] for idx in cookie_idxs]
    else:
        # If segments2find is empty, find any cookies that share segments
        for idx1,segment_lib in enumerate(segments):
            if(len(segment_lib) > 1):
                for idx2 in range(1,len(segments)):
                    if(len(segments[idx2]) > 1):
                        if( any( seg in segment_lib for seg in segments[idx2] ) ):
                            cookie_idxs.append(idx1)
                            cookie_idxs.append(idx2)
        return [cookies[idx] for idx in cookie_idxs]

def main():
    # Ops to do
    data = sys.stdin.readlines()
    cookies,segments = get_data(data)

    # Part A
    found_cookies = find_cookies(['D08734_72525','D08734_74065'],cookies,segments)
    print(found_cookies)

    # Part B
    found_cookies = find_cookies([],cookies,segments)
    print(found_cookies)

main()