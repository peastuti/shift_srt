import srt_shift
import sys

def printUsage():
    print("\n\tshift_srt [namefile] [-b = backward/-f = forward] [seconds 00.000]\n")

arguments = sys.argv

if arguments[1] == "help":
    printUsage()
else:
    try:
        try:
            res = ''
            delta = float(arguments[3])

            if (arguments[2] == '-b'):
                res = srt_shift.shiftSrt(arguments[1], 'backward', delta)
            if (arguments[2] == '-f'):
                res = srt_shift.shiftSrt(arguments[1], 'forward', delta)

            if(res != ''):
                print("\nSUCCESS! " + res.name + " is ready\n")
            else: print("Unexpected Error! Check the parameters!")

        except IndexError:
            print("ERROR: Some parameters are missing!")

    except ValueError:
        print("ERROR: the delta must be a number!\n")




