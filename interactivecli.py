###Enter unit number variable###
unit=raw_input("Welcome to the tenant portal! Please enter your unit number: ")


import os,time #import libraries because Asthetics make me happy...
os.system('clear')



print 'What would you like to accomplish today?'

time.sleep(1)
print 'Please select a number 1 - 4, then press enter:'
time.sleep(1)
print '1. Make a manintenances request\n 2. Make a purchase \n 3. Reserve a common area\n 4. Submit a complaint on one of our common areas'

type=raw_input('I would like to: ')

### Convert string to int type ##

type = int(type)
#####################################Maintenance requests###################################
if type == 1:
        os.system('clear')
        issue=raw_input("Please specify your maintenance request: ")

        os.system('clear')
        print "Thank you, tenant at unit %s. Your request for maintenance do deal with %s has been received!" %(unit, issue)


##################################### Payment / Purchase ###################################

elif type == 2:
        os.system('clear')
        print ("Okay, so you want to give us money! How nice of you : ) ")

        commodity=raw_input("What are you purchasing today? ")

        os.system('clear')

        print "Thank you, tenant at unit %s. Your request to purchase a %s has been received!" %(unit, commodity)


##################################### Room Booking ###################################


elif type == 3:
        os.system('clear')
        print 'Our Conference, Poker, and Game room as well as our Movie Theater are available for booking.'
        room = raw_input("Which of our rooms would you like to book? ")

        date=raw_input("What dates? ")
        duration=raw_input("How long will you be loitering *cough cough* I mean, occupying the facilites? ")

        os.system('clear')

        print "Thank you tenant at unit %s. Your request to reserve our %s on %s for %s has been received!" %(unit, room, date, duration)


##################################### Complaint Submission ###################################


elif type == 4:
        os.system('clear')
        location=raw_input("What common area is this feedback for? ")

        issue=raw_input("Please describe the complaint:")

        os.system('clear')

        print "Thank you, tenant at unit %s. We will have someone follow up on %s in regards to our %s." %(unit, issue, location)



else:    ## default ##
        os.system('clear')
        print ("womp womp. Try again...")
