# initial-setup.csh

set IS_EXEC = /usr/bin/initial-setup
set IS_UNIT = initial-setup-text.service

# check if the Initial Setup unit is enabled and the executable is available
if ( { systemctl -q is-enabled $IS_UNIT } && -x $IS_EXEC ) then
    # check if we're not on 3270 terminal and root
    if (( `/sbin/consoletype` == "pty" ) && ( `/usr/bin/id -u` == 0 )) then
        $IS_EXEC && systemctl -q disable $IS_UNIT
    endif
endif
