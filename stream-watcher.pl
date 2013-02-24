#!/usr/bin/perl
my $blanked = 0;
my $pid = open (IN, "xscreensaver-command -watch |");
while (<IN>) {
	if (m/^UNBLANK/) {
		# TODO: kill only this mplayer's PID
		system("/usr/bin/pkill", "-9", "mplayer");
		# TODO: kill only this rtmpdump PID
		system("/usr/bin/pkill", "-9", "rtmpdump");
		## kill only this pid(s)
		kill 9, $pid;
		break;
	}
}
close(IN);
exit 0;
