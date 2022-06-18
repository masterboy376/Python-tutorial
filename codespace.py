import pendulum
past = pendulum.now().subtract(minutes=2)
past.diff_for_humans()