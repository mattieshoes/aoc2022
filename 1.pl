#!/usr/bin/perl

use List::Util "sum";
@n = split(/\n\n/, `cat 1.txt`);
foreach (@n) {
    push(@elf, sum(split(/\n/)));
}
@elf = sort {$b <=> $a} (@elf);
print "$elf[0]\n";
print $elf[0]+$elf[1]+$elf[2] . "\n";
