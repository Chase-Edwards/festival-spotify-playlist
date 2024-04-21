import json

lineup = """A LITTLE SOUND - ACE AURA - ALLEYCVT - ALYCIA - BEN VERSE - BISOUX - BLVNKSPVCE - BOOGIE T  - BREDREN - BUUNSHIN - CAITC - CRITICAL SOUNDSYSTEM FT. KASRA, CALYX & SPECTRAL - CUVURS - ESKEI83 - ETHERWOOD - FLAVA D - FRED V & GRAFIX - GENTLEMEN’S CLUB - GEST - GOSHIKI -HAMDI - HAMRO - HOLLY - IDLE DAYS - IMANU - IVY LAB - JAKES - JON CASEY - KANINE - KOMPANY - LATTE - LIXED - MACKY GEE - METRIK - MIDNIGHT TYRANNOSAURUS - MISCALL - MOLLIE COLLINS - MOTHER - LOTUS - MUERTE - MVRDA - NATTE VISSTICK - NERSHA - P MONEY - P MONEY X WHINEY - PARRA MIER - POLA & BRYSON - PREMIUM - RIANA HOLLEY - RUDIM3NTAL - SHAWIYA TRIBE - SHIVERZ - SKAMM - SPAG HEDDY - SQISHI - SUB MOTIONZ - SUDLEY - SWEETTOOTH - SYNOXIS - T-LEX - TANTRON - TECHNIMATIC - TESEN - THE PANACEA - THE PARTYSQUAD - TOXINATE - UNGLUED - USED - VDV - WAEYS - WINSLOW - AC13 - AMPLIFY - ANNIX - ARCANDO - ATMOS - AUDIO - AUTOMHATE - BADKLAAT - BARELY ALIVE - BASSTRICK - BASSTRIPPER - BLACK SUN EMPIRE - BLACKLEY - CALYX - CAMOUFLY - CAPTAIN BASS  - CODD DUBZ - DIRTYPHONICS - DISRUPTA - DJ CRAZE - DJ HYPE - DUB FX - DUX N BASS - FANTASM - FLOWANASTASIA - GEORGIE RIOT - GRAFIX - IMANU - IN THE LAB -JOKER - KARA - KOAN SOUND - KOVEN - LIMITED - MAD DUBZ - MÆNA - MAKLA - MEGALODON - MICHAEL SPARKS - MIDNIGHT CVLT - MODESTEP - MUTATED FORMS - MYSELOR - NEONLIGHT - NITEPUNK - NYMFO - ONE87 - P MONEY - PHASEONE - REAPER - RENÉ LAVICE - REQUAKE - ROBITOS - SASASAS - SHOCKONE - SIR SPYRO - SKULPT - SOTA - SUB ZERO - SYZY - THE UPBEATS - TNA - TSUKI - TYR KOHOUT - UPGRADE - VASTIVE - VERSA - VOLUNT BARBATI - VOYD - ZERO - 19825 - 3D GIF DUBSTEP - AAZAR - ABYSSAL MUSIC - AKEOS - ANDROMEDIK - ANULIX - APHRODITE - ATLIENS - BADJOKES - BORN ON ROAD - BOSSFIGHT - CAMO & KROOKED - D*MINDS - DAN LEE - DANNY BYRD - DEADROOM - DIKKE BAAP - DIVICIOUX - DJ RAP - DOINKGOD - DR USHUU - DUB ELEMENTS - ENTA - EPROM - EXPLORERS OF THE INTERNET - FORMULA - GLADDE PALING - GLOCKZ - H808 - HABSTRAKT - HATO - HOL! - IITYX - INSTAR - INVICTA AUDIO - JAKES - JESSICA - AUDIFFRED - K MOTIONZ - KENDRICK - LOLALITA - LOOMPASKETTEE - MANDIDEXTROUS - MEF JUS - MIA - KODEN - MIDAS TOUCH - MOLEY - MURDOCK - MYU:SA - NATTY LOU - NOIR - PEGBOARD NERDS - PENDULUM - PHIBES - ROI - RONI SIZE - RUN IN THE JUNGLE -SAMPLIFIRE - SIMULA - SKANTIA - SOLTAN - SPINSCOTT - SVDDEN DEATH - VAMPA - VIRTUAL RIOT - WALTUR - WHALES - YAKZ - YVM3"""

lineup_list = lineup.split(" - ")
lineup_json = json.dumps(lineup_list)

print(lineup_json)

with open('.\\data\\lineup.json', 'w') as file:
    file.write(lineup_json)
    file.close()