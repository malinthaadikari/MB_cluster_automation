from subprocess import call
call("while ! echo exit | nc 10.0.2.12 9445; do sleep 10; done", shell="True")
print "malintha"
