
#include <cstdlib>
#include <iostream>
#include <string>
#include <time.h>

using namespace std;

char * now() {
  time_t rawtime;
  time(&rawtime);
  return ctime (&rawtime);
}

#include <iostream>
using namespace std;

enum State {
    OFF_DUTY_STATE,
    ON_DUTY_STATIONARY_STATE,
    ON_DUTY_MOVING_STATE,
    END_STATE,
  };
enum Event {
    END_EVENT,
    ON_DUTY_EVENT,
    START_EVENT,
    OFF_DUTY_EVENT,
    STOP_EVENT,
		INVALID_EVENT
  };

const char * EVENT_NAMES[] = {
	"END",
	"ON_DUTY",
	"START",
	"OFF_DUTY",
	"STOP",
};
Event get_next_event();

Event string_to_event(string event_string) {
	if (event_string == "END") {return END_EVENT;}
	if (event_string == "ON_DUTY") {return ON_DUTY_EVENT;}
	if (event_string == "START") {return START_EVENT;}
	if (event_string == "OFF_DUTY") {return OFF_DUTY_EVENT;}
	if (event_string == "STOP") {return STOP_EVENT;}
	return INVALID_EVENT;
}

int hos(State initial_state) {
	State state = initial_state;
	Event event;
	while (true) {
		switch(state) {

      case OFF_DUTY_STATE:
        cerr << "stateOFF_DUTY" << endl;
        // code for OFF_DUTY_STATE

        event = get_next_event();
        cerr << "event " << EVENT_NAMES[event] << endl;
        switch (event) {
