
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

using namespace std;
  enum State {
    s_OFF_DUTY,
    s_ON_DUTY_STATIONARY,
    s_ON_DUTY_MOVING,
    s_END,
  };
  enum Event {
    e_OFF_DUTY,
    e_START,
    e_STOP,
    e_ON_DUTY,
    e_END,
  };

const char * Event_NAMES[] = {
	"OFF_DUTY"
	"START"
	"STOP"
	"ON_DUTY"
	"END"
};
Event get_next_event();

Event string_to_event(string event_string) {
	if (event_string == "OFF_DUTY") {return "OFF_DUTY_EVENT";}
	if (event_string == "START") {return "START_EVENT";}
	if (event_string == "STOP") {return "STOP_EVENT";}
	if (event_string == "ON_DUTY") {return "ON_DUTY_EVENT";}
	if (event_string == "END") {return "END_EVENT";}
	return INVALID_EVENT;
}

int hos(State initial_state) {
	State state = initial_state;
	while (true) {
		switch(state) {

      case s_OFF_DUTY:
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
      case s_ON_DUTY_STATIONARY:
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
      case s_ON_DUTY_MOVING:
        cout << "driver is moving" << endl;

        event = get_next_event();
        switch (event) {
          case e_STOP:
            
            state = s_ON_DUTY_STATIONARY;
          break;
        }
        break;
      case s_END:
        
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

