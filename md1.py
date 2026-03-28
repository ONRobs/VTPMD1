import hfst

generator = hfst.compile_lexc_file('md1.lexc')

InsertJ = hfst.regex('[..] -> j || [b | f | m | p | v] _ "^" M')

ZNReplacement = hfst.regex('z n -> ž ņ ||  _ "^" M')
DReplacement = hfst.regex('d -> ž ||  _ "^" M')
TReplacement = hfst.regex('t -> š ||  _ "^" M')

MCleanup = hfst.regex('M -> 0')
Cleanup = hfst.regex('"^" -> 0')

cascade = hfst.compose((generator, InsertJ, ZNReplacement, DReplacement, TReplacement, MCleanup, Cleanup))

for noun in ["med", "al", "liet", "up", "zvaigzn", "cepur", "nakt", "aus", "ac", "ļaud"]:
    for number in ["Sg", "Pl"]:
        for form in ["Nom", "Gen", "Dat", "Acc", "Loc"]:
            result = cascade.lookup(noun + "+N+" + number + "+" + form)
            if result:
                print(noun + "+N+" + number + "+" + form + " - " + result[0][0].replace("@_EPSILON_SYMBOL_@", ""))
            else:
                print(noun + "+N+" + number + "+" + form + " - ")
