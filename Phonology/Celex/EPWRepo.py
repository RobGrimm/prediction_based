import os
import cPickle


def get_file_path():
    return os.path.dirname(os.path.realpath(__file__))


class EPWRepo(object):

    def __init__(self, words_to_phonemes_dict):
        """
        Class wrapper around dictionary mapping word strings to sequences of phonemes and primary stress vectors,
        extracted from the CELEX database.
        """
        self.token_to_phonemes_dict = words_to_phonemes_dict

        self.additional_phon_forms = {'yucky': 'jVkI',
                                      'pajamas': 'p@JAm@z',
                                      'mommy': 'mVmI',
                                      'popsicle': 'pOpsIk@l',
                                      'yogurt': 'j@Ug@t',
                                      'firetruck': 'faI@trVk',
                                      'next_to': 'nEkst@',
                                      'cheerios': 'CirI@Uz',
                                      'mhm': '@Um',
                                      'have_to': 'h&ft@',
                                      'thank_you': 'T&Nkju',
                                      'uhhuh': '@h@',
                                      'ross': 'rOs',
                                      'out_of': 'aUd@v',
                                      "willn't": 'wIlnt',
                                      'color': 'kal@',
                                      'ya': 'ja',
                                      'as_well': '@swEl',
                                      'got_to': 'gOt@',
                                      'becky': 'bEki',
                                      'abe': 'EIb',
                                      'cathy': 'k&Ti',
                                      'sarah': 's&ra',
                                      'ruth': 'ruT',
                                      'nina': 'nina',
                                      'nicole': 'n@kOl',
                                      'anne': '&n',
                                      'lots_of': 'lOts@v',
                                      'aran': '&r@n',
                                      'a_lot_of': '@lOd@v',
                                      'em': '@m',
                                      'caroline': 'k&r@lIn',
                                      'uhu': '@h@',
                                      'goin': 'g@UIn',
                                      'has_to': 'h&st@',
                                      'doggie': 'dOgI',
                                      'mummie': 'mvmI',
                                      'anymore': 'EnImO',
                                      'byebye': 'baIbaI',
                                      "anna's": '&n@z',
                                      'david': 'deIvId',
                                      'yep': 'jep',
                                      'horsie': 'hOsI',
                                      'favorite': 'feIvrIt',
                                      'liz': 'lIz',
                                      'uhoh': '@h@h',
                                      'colors': 'kVl@z',
                                      'paul': 'pOl',
                                      'andy': '&ndI',
                                      'nana': 'n&nA',
                                      'pottie': 'pOtI',
                                      'baba': 'b&b@',
                                      'doin': 'dUIn',
                                      'whee': 'wi',
                                      'so_that': 's@UD&t',
                                      'matthew': 'm&Tju',
                                      'gordon': 'gOd@n',
                                      'ummhm': '@m',
                                      'santa': 's&nt@',
                                      'babys': 'beIbIz',
                                      'motorcycle': 'm@Ut@saIkl',
                                      'gail': 'geIl',
                                      'uhhum': '@m',
                                      'santa_claus': 's&nt@klOz',
                                      'joel': 'D@Ul',
                                      'conor': 'kOn@',
                                      'night_night': 'naItnaIt',
                                      'pingu': 'pINu',
                                      'henry': 'hEnrI',
                                      'james': 'DeImz',
                                      'och': 'Oh',
                                      'look_it': 'lUkIt',
                                      'all_gone': 'OlgOn',
                                      'graeme': 'greIm',
                                      'percy': 'p3sI',
                                      'joey': 'D@UI',
                                      'somethin': 'sVmpTIn',
                                      'duplo': 'dupl@U',
                                      "mummy'll": 'mVmIl',
                                      'chris': 'kris',
                                      'fraser': 'freIz@',
                                      "man's": 'm&nz',
                                      'television': 'tEl@vIZn',
                                      'miffy': 'mIfI',
                                      'postman_pat': 'p@Usm@np&t',
                                      'linda': 'lInd@',
                                      'maggie': 'm&gI',
                                      'yup': 'jVp',
                                      'sukie': 'sUkI',
                                      'ahhah': '@h@',
                                      'julia': 'DulI@',
                                      'ssh': 's',
                                      'gabriella': 'g&brIEl',
                                      'urs': 'urz',
                                      'jamie': 'DeImI',
                                      'each_other': 'iCVD@',
                                      'nonna': 'nOn@',
                                      'lego': 'lEg@U',
                                      'oop': 'Up',
                                      'jason': 'DeIs@n',
                                      'upside': 'VpsaId',
                                      'oo': '@U',
                                      'kent': 'kEnt',
                                      'rachel': 'reIc@l',
                                      'tony': 't@UnI',
                                      'my_goodness': 'mIgUdn@s',
                                      'barbara': 'bAb@rA',
                                      'cha': 'CV',
                                      'comin': 'kVmIn',
                                      'lemme': 'lEmI',
                                      'duckie': 'dVkI',
                                      'dat': 'd&t',
                                      'oy': 'OI',
                                      'burger': 'b3g@',
                                      'gettin': 'gEtIn',
                                      'ought_to': 'Ot@',
                                      'oliver': 'OlIv@',
                                      'joe': 'D@U',
                                      'granddad': 'gr&nd&d',
                                      'samantha': 's@m&nT@',
                                      'yummy': 'jVmI',
                                      'umhum': '@mh@m',
                                      "that's": 'D&ts',
                                      "it's": 'Its',
                                      "what's": 'hwOts',
                                      "he's": 'hIz',
                                      "there's": 'D@z',
                                      "let's": 'lEts',
                                      "where's": 'hwE@z',
                                      "who's": 'huz',
                                      "she's": 'SIz',
                                      "here's": 'hI@z',
                                      "mummy's": 'mVmIz',
                                      "one's": 'wVnz',
                                      'marky': 'mAkI',
                                      "daddy's": 'd&dIz',
                                      "color's": 'kVl@z',
                                      "mommy's": 'mVmIz',
                                      'uhuh': '@h@',
                                      "dolly's": 'dOlIz',
                                      "how's": 'haUz',
                                      "baby's": 'beIbIz',
                                      "caroline's": 'k&r@lInz',
                                      "anne's": '&nz',
                                      "marky's": 'mAkIz',
                                      "carl's": 'kAlz',
                                      "grandma's": 'gr&nmAz',
                                      "somebody's": 'sVmbOdIz',
                                      "nana's": 'n&nAz',
                                      "rachel's": 'reIClz',
                                      "boy's": 'bOIz',
                                      "puppys": 'pVpIz',
                                      "nina's": 'ninaz',
                                      "dog's": 'dOgz',
                                      "cat's": 'k&ts',
                                      "karen": 'k&r@nz',
                                      "andy's": '&ndIz',
                                      "edward": 'EdwOd',
                                      "panda's": 'p&ndAz',
                                      'hmm': 'h@m',
                                      'as_soon_as': '&zsun&z',
                                      'nappie': 'n&pI',
                                      'coloring': 'kVl@rIN',
                                      "mummie's": 'mVmIz',
                                      'brian': 'braI@n',
                                      "girl's": 'g3lz',
                                      'no_no': 'n@Un@U',
                                      'snoopy': 'snupI',
                                      'stuart': 'stju@t',
                                      'ursula': 'urs@lA',
                                      'melissa': 'm@lIsA',
                                      "eve's": 'iv',
                                      'strawberrys': 'strObrIz',
                                      'in_case': 'InkeIs',
                                      'derwood': 'd3rwUd',
                                      'talkin': 'tOkIn',
                                      'vegetables': 'vEDt@blz',
                                      'cromer': 'kr@Um@',
                                      'ach': 'Vh',
                                      'awoh': 'VwOh',
                                      'lucy': 'lusI',
                                      "teddy's": 'tEdIz',
                                      'courtney': 'kOtnI',
                                      'tellie': 'tElI',
                                      "pingu's": 'pINuz',
                                      'pennys': 'pEnIz',
                                      'remi': 'rEmI',
                                      'chantilly': 'C&nt@lI',
                                      "lady's": 'leIdIz',
                                      "train's": 'treInz',
                                      'noddy': 'nOdI',
                                      'yuck': 'jVk',
                                      'rid': 'rId',
                                      'colin': 'kOlIn',
                                      "mother's": 'mVD@z',
                                      'caitlin': 'keItlIn',
                                      'lookin': 'lUkIn',
                                      "car's": 'kAz',
                                      'yay': 'jeI',
                                      'luke': 'luk',
                                      'morag': 'mOr&g',
                                      'good_night': 'gUdnaIt',
                                      'donna': 'dOnA',
                                      'bernard': 'b@nAd',
                                      'dexter': 'dEkst@',
                                      "doll's": 'dOlz',
                                      "maggie's": 'm&gIz',
                                      'cmon': 'k@mOn',
                                      'liam': 'lI@m',
                                      'robert': 'rOb@t',
                                      'pooh_bear': 'pubE@',
                                      'claus': 'klOz',
                                      "tiger's": 'taIg@z',
                                      "rosie": 'r@UzI',
                                      'hafta': 'h&ft@',
                                      "mama's": 'mAm@z',
                                      'froggie': 'frOgI',
                                      'choo': 'Cu',
                                      'andrew': '&ndru',
                                      'carwash': 'kAwOS',
                                      'ann_marie': '&nmE@rI',
                                      'donald': 'dOn@ld',
                                      'ellie': 'ElI',
                                      'program': 'pr@Ugr&m',
                                      "henry's": 'hEnrIz',
                                      'michelle': 'm@SEl',
                                      "whyn't": 'hwaInt',
                                      "sister's": 'sIst@z',
                                      'gimme': 'gImI',
                                      'jesus': 'Diz@z',
                                      'jess': 'DEs',
                                      'spencer': 'spEns@',
                                      'brett': 'brEt',
                                      'you_all': 'juOl',
                                      "sarah's": 's&raz',
                                      'christopher': 'krisOf@',
                                      'potatos': 'p@teIt@Uz',
                                      'wha': 'hwOt',
                                      'dis': 'dIs',
                                      'nothin': 'nVTIn',
                                      'le': 'lE',
                                      "percy's": 'p3sIz',
                                      'kate': 'keIt',
                                      "monkey's": 'mVNkIz',
                                      'poo': 'pu',
                                      'comere': 'k@mI@',
                                      'sylvia': 'SIlvIA',
                                      'da': 'dA',
                                      'denver': 'dEnv@',
                                      'sam': 's&m',
                                      'ewok': 'IwOk',
                                      'mia': 'mIA',
                                      "doctor's": 'dOkt@z'}


        self.additional_primary_stress = {'yucky': [1, 0, 0],
                                          'pajamas': [0, 1, 0],
                                          'mommy': [1, 0, 0],
                                           'yogurt': [1, 0, 0],
                                          'popsicle': [1, 0, 0],
                                          'firetruck': [1, 0, 0],
                                          'next_to': [1, 0, 0],
                                          'cheerios': [1, 0, 0],
                                          'mhm': [0, 0, 0],
                                          'have_to': [1, 0, 0],
                                          'thank_you': [1, 0, 0],
                                          'uhhuh': [0, 0, 0],
                                          'ross': [1, 0, 0],
                                          'out_of': [1, 0, 0],
                                          "willn't": [1, 0, 0],
                                          'color': [1, 0, 0],
                                          'ya': [1, 0, 0],
                                          'as_well': [0, 1, 0],
                                          'got_to': [1, 0, 0],
                                          'becky': [1, 0, 0],
                                          'abe': [1, 0, 0],
                                          'cathy': [1, 0, 0],
                                          'sarah': [1, 0, 0],
                                          'ruth': [1, 0, 0],
                                          'nina': [1, 0, 0],
                                          'nicole': [0, 1, 0],
                                          'anne': [1, 0, 0],
                                          'lots_of': [1, 0, 0],
                                          'aran': [1, 0, 0],
                                          'a_lot_of': [0, 1, 0],
                                          'em': [0, 0, 0],
                                          'caroline': [1, 0, 0],
                                          'uhu': [0, 0, 0],
                                          'goin': [1, 0, 0],
                                          'has_to': [1, 0, 0],
                                          'doggie': [1, 0, 0],
                                          'mummie': [1, 0, 0],
                                          'anymore': [1, 0, 0],
                                          'byebye': [1, 0, 0],
                                          "anna's": [1, 0, 0],
                                          'david': [1, 0, 0],
                                          'yep': [1, 0, 0],
                                          'horsie': [1, 0, 0],
                                          'favorite': [1, 0, 0],
                                          'liz': [1, 0, 0],
                                          'uhoh': [0, 0, 0],
                                          'colors': [1, 0, 0],
                                          'paul': [1, 0, 0],
                                          'andy': [1, 0, 0],
                                          'nana': [1, 0, 0],
                                          'pottie': [1, 0, 0],
                                          'baba': [1, 0, 0],
                                          'doin': [1, 0, 0],
                                          'whee': [1, 0, 0],
                                          'so_that': [0, 1, 0],
                                          'matthew': [1, 0, 0],
                                          'gordon': [1, 0, 0],
                                          'ummhm': [0, 0, 0],
                                          'santa': [1, 0, 0],
                                          'babys': [1, 0, 0],
                                          'motorcycle': [1, 0, 0],
                                          'gail': [1, 0, 0],
                                          'uhhum': [0, 0, 0],
                                          'santa_claus': [1, 0, 0],
                                          'joel': [1, 0, 0],
                                          'conor': [1, 0, 0],
                                          'night_night': [1, 0, 0],
                                          'pingu': [1, 0, 0],
                                          'henry': [1, 0, 0],
                                          'james': [1, 0, 0],
                                          'och': [0, 0, 0],
                                          'look_it': [1, 0, 0],
                                          'all_gone': [0, 1, 0],
                                          'graeme': [1, 0, 0],
                                          'percy': [1, 0, 0],
                                          'joey': [1, 0, 0],
                                          'somethin': [1, 0, 0],
                                          'duplo': [1, 0, 0],
                                          "mummy'll": [1, 0, 0],
                                          'chris': [1, 0, 0],
                                          'fraser': [1, 0, 0],
                                          "man's": [1, 0, 0],
                                          'television': [1, 0, 0],
                                          'miffy': [1, 0, 0],
                                          'postman_pat': [0, 0, 1],
                                          'linda': [1, 0, 0],
                                          'maggie': [1, 0, 0],
                                          'yup': [1, 0, 0],
                                          'sukie': [1, 0, 0],
                                          'ahhah': [0, 0, 0],
                                          'julia': [1, 0, 0],
                                          'ssh': [0, 0, 0],
                                          'gabriella': [1, 0, 0],
                                          'urs': [1, 0, 0],
                                          'jamie': [1, 0, 0],
                                          'each_other': [1, 0, 0],
                                          'nonna': [1, 0, 0],
                                          'lego': [1, 0, 0],
                                          'oop': [0, 0, 0],
                                          'jason': [0, 0, 0],
                                          'upside': [0, 1, 0],
                                          'oo': [0, 0, 0],
                                          'kent': [1, 0, 0],
                                          'rachel': [1, 0, 0],
                                          'tony': [1, 0, 0],
                                          'my_goodness': [0, 1, 0],
                                          'barbara': [1, 0, 0],
                                          'cha': [1, 0, 0],
                                          'comin': [1, 0, 0],
                                          'lemme': [1, 0, 0],
                                          'duckie': [1, 0, 0],
                                          'dat': [0, 0, 0],
                                          'oy': [1, 0, 0],
                                          'burger': [1, 0, 0],
                                          'gettin': [1, 0, 0],
                                          'ought_to': [1, 0, 0],
                                          'oliver': [1, 0, 0],
                                          'joe': [1, 0, 0],
                                          'granddad': [0, 1, 0],
                                          'samantha': [0, 1, 0],
                                          'yummy': [1, 0, 0],
                                          'umhum': [0, 0, 0],
                                          "that's": [1, 0, 0],
                                          "it's": [1, 0, 0],
                                          "what's": [1, 0, 0],
                                          "he's": [1, 0, 0],
                                          "there's": [1, 0, 0],
                                          "let's": [1, 0, 0],
                                          "where's": [1, 0, 0],
                                          "who's": [1, 0, 0],
                                          "she's": [1, 0, 0],
                                          "here's": [1, 0, 0],
                                          "mummy's": [1, 0, 0],
                                          "one's": [1, 0, 0],
                                          'marky': [1, 0, 0],
                                          "daddy's": [1, 0, 0],
                                          "color's": [1, 0, 0],
                                          "mommy's": [1, 0, 0],
                                          'uhuh': [0, 0, 0],
                                          "dolly's": [1, 0, 0],
                                          "how's": [1, 0, 0],
                                          "baby's": [1, 0, 0],
                                          "caroline's": [1, 0, 0],
                                          "anne's": [1, 0, 0],
                                          "marky's": [1, 0, 0],
                                          "carl's": [1, 0, 0],
                                          "grandma's": [0, 1, 0],
                                          "somebody's": [0, 1, 0],
                                          "nana's": [1, 0, 0],
                                          "rachel's": [1, 0, 0],
                                          "boy's": [1, 0, 0],
                                          "puppys": [1, 0, 0],
                                          "nina's": [1, 0, 0],
                                          "dog's": [1, 0, 0],
                                          "cat's": [1, 0, 0],
                                          "karen": [1, 0, 0],
                                          "andy's": [1, 0, 0],
                                          "edward": [1, 0, 0],
                                          "panda's": [1, 0, 0],
                                          'hmm': [0, 0, 0],
                                          'as_soon_as': [0, 1, 0],
                                          'nappie': [1, 0, 0],
                                          'coloring': [1, 0, 0],
                                          "mummie's": [1, 0, 0],
                                          'brian': [1, 0, 0],
                                          "girl's": [1, 0, 0],
                                          'no_no': [1, 0, 0],
                                          'snoopy': [1, 0, 0],
                                          'stuart': [1, 0, 0],
                                          'ursula': [1, 0, 0],
                                          'melissa': [0, 1, 0],
                                          "eve's": [1, 0, 0],
                                          'strawberrys': [1, 0, 0],
                                          'in_case': [0, 1, 0],
                                          'derwood': [1, 0, 0],
                                          'talkin': [1, 0, 0],
                                          'vegetables': [1, 0, 0],
                                          'cromer': [1, 0, 0],
                                          'ach': [0, 0, 0],
                                          'awoh': [0, 1, 0],
                                          'lucy': [1, 0, 0],
                                          "teddy's": [1, 0, 0],
                                          'courtney': [1, 0, 0],
                                          'tellie': [1, 0, 0],
                                          "pingu's": [1, 0, 0],
                                          'pennys': [1, 0, 0],
                                          'remi': [1, 0, 0],
                                          'chantilly': [1, 0, 0],
                                          "lady's": [1, 0, 0],
                                          "train's": [1, 0, 0],
                                          'noddy': [1, 0, 0],
                                          'yuck': [1, 0, 0],
                                          'rid': [1, 0, 0],
                                          'colin': [1, 0, 0],
                                          "mother's": [1, 0, 0],
                                          'caitlin': [1, 0, 0],
                                          'lookin': [1, 0, 0],
                                          "car's": [1, 0, 0],
                                          'yay': [1, 0, 0],
                                          'luke': [1, 0, 0],
                                          'morag': [1, 0, 0],
                                          'good_night': [0, 1, 0],
                                          'donna': [1, 0, 0],
                                          'bernard': [0, 1, 0],
                                          'dexter': [1, 0, 0],
                                          "doll's": [1, 0, 0],
                                          "maggie's": [1, 0, 0],
                                          'cmon': [0, 1, 0],
                                          'liam': [1, 0, 0],
                                          'robert': [1, 0, 0],
                                          'pooh_bear': [1, 0, 0],
                                          'claus': [1, 0, 0],
                                          "tiger's": [1, 0, 0],
                                          "rosie": [1, 0, 0],
                                          'hafta': [1, 0, 0],
                                          "mama's": [1, 0, 0],
                                          'froggie': [1, 0, 0],
                                          'choo': [1, 0, 0],
                                          'andrew': [1, 0, 0],
                                          'carwash': [1, 0, 0],
                                          'ann_marie': [0, 1, 0],
                                          'donald': [1, 0, 0],
                                          'ellie': [1, 0, 0],
                                          'program': [1, 0, 0],
                                          "henry's": [1, 0, 0],
                                          'michelle': [0, 1, 0],
                                          "whyn't": [1, 0, 0],
                                          "sister's": [1, 0, 0],
                                          'gimme': [1, 0, 0],
                                          'jesus': [1, 0, 0],
                                          'jess': [1, 0, 0],
                                          'spencer': [1, 0, 0],
                                          'brett': [1, 0, 0],
                                          'you_all': [0, 1, 0],
                                          "sarah's": [1, 0, 0],
                                          'christopher': [1, 0, 0],
                                          'potatos': [0, 1, 0],
                                          'wha': [1, 0, 0],
                                          'dis': [1, 0, 0],
                                          'nothin': [1, 0, 0],
                                          'le': [1, 0, 0],
                                          "percy's": [1, 0, 0],
                                          'kate': [1, 0, 0],
                                          "monkey's": [1, 0, 0],
                                          'poo': [1, 0, 0],
                                          'comere': [1, 0, 0],
                                          'sylvia': [1, 0, 0],
                                          'da': [1, 0, 0],
                                          'denver': [1, 0, 0],
                                          'sam': [1, 0, 0],
                                          'ewok': [1, 0, 0],
                                           'mia': [1, 0, 0],
                                           "doctor's": [1, 0, 0]}


    def get_phonologicalform(self, word):

        if word.endswith("'s"):

            word.rstrip("'s")
        elif word.endswith("'s"):
            word.rstrip("'s")

        try:
            return self.token_to_phonemes_dict['phonemes'][word]
        except KeyError:
            return self.get_phonologicalform_additional(word)

    def get_phonologicalform_additional(self, word):
        try:
            return self.additional_phon_forms[word]
        except KeyError:
            raise Exception("Don't have a sequence of phonemes for word: %s "
                            "You probably need to hard-code that (add to self.additional_phon_forms" % word)

    def get_primary_stress_pattern(self, word):
        try:
            return self.token_to_phonemes_dict['primary_stress'][word]
        except KeyError:
            return self.get_primary_stress_additional(word)

    def get_primary_stress_additional(self, token):
        try:
            return self.additional_primary_stress[token]
        except KeyError:
            raise Exception("Don't have a stress pattern for word: %s "
                            "You probably need to hard-code that (add to self.additional_primary_stress" % token)


epw = get_file_path() + '/epw/epw.p'
epw_dict = cPickle.load(open(epw, "rb"))
epw_repo = EPWRepo(epw_dict)