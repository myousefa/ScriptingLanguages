
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
    START_EVENT,
    ON_DUTY_EVENT,
    END_EVENT,
    STOP_EVENT,
    OFF_DUTY_EVENT,
		INVALID_EVENT
  };

const char * Event_NAMES[] = {
	"START"
	"ON_DUTY"
	"END"
	"STOP"
	"OFF_DUTY"
};
Event get_next_event();

Event string_to_event(string event_string) {
	if (event_string == "START") {return "START_EVENT";}
	if (event_string == "ON_DUTY") {return "ON_DUTY_EVENT";}
	if (event_string == "END") {return "END_EVENT";}
	if (event_string == "STOP") {return "STOP_EVENT";}
	if (event_string == "OFF_DUTY") {return "OFF_DUTY_EVENT";}
	return INVALID_EVENT;
}

int hos(State initial_state) {
	State state = initial_state;
	while (true) {
		switch(state) {

      case OFF_DUTY_STATE:
        // code for OFF_DUTY_STATE

        event = get_next_event();
        switch (event) {
          case e_END:
            
cout << "th-th-that's all, folks." << endl;
exit(EXIT_SUCCESS);

            state = s_END;
          break;
          case e_ON_DUTY:
            
cout << "driver coming on duty " << now();

            state = s_ON_DUTY_STATIONARY;
          break;
        }
        break;
      case ON_DUTY_STATIONARY_STATE:
        cout << "driver is stationary" << endl;

        event = get_next_event();
        switch (event) {
          case e_OFF_DUTY:
            cout << "driver coming off duty " << now();
            state = s_OFF_DUTY;
          break;
          case e_START:
            
            state = s_ON_DUTY_MOVING;
          break;
        }
        break;
      case ON_DUTY_MOVING_STATE:
        cout << "driver is moving" << endl;

        event = get_next_event();
        switch (event) {
          case e_STOP:
            
            state = s_ON_DUTY_STATIONARY;
          break;
        }
        break;
      case END_STATE:
        
        event = get_next_event();
        switch (event) {
        }
        break;
    }
  }
}

Event get_next_event() {
   string event_string;
   cin >> event_string;
   return string_to_event(event_string);
}
int main() {
    int result = hos(OFF_DUTY_STATE);
    return result >= 0 ? EXIT_SUCCESS : EXIT_FAILURE;
}

