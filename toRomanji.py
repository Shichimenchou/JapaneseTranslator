import sys

inp = sys.argv[1]
out = ''

smol = ['ゃ', 'ゅ', 'ょ']
chisaiTsu = False

for i in range(0, len(inp)):
	c = inp[i]
	if i != len(inp) - 1:
		if inp[i+1] in smol:
			c += inp[i+1]
			i += 1
	
	if c == 'っ' or c == 'ッ':
		chisaiTsu = True
		continue
	if chisaiTsu:
		if c == 'か' or c == 'カ': out += 'kka'
		elif c == 'き' or c == 'キ': out += 'kki'
		elif c == 'く' or c == 'ク': out += 'kku'
		elif c == 'け' or c == 'ケ': out += 'kke'
		elif c == 'こ' or c == 'コ': out += 'kko'
		elif c == 'さ' or c == 'サ': out += 'ssa'
		elif c == 'し' or c == 'シ': out += 'sshi'
		elif c == 'す' or c == 'ス': out += 'ssu'
		elif c == 'せ' or c == 'セ': out += 'sse'
		elif c == 'そ' or c == 'ソ': out += 'sso'
		elif c == 'た' or c == 'タ': out += 'tta'
		elif c == 'ち' or c == 'チ': out += 'cchi'
		elif c == 'つ' or c == 'ツ': out += 'ttsu'
		elif c == 'て' or c == 'テ': out += 'tte'
		elif c == 'と' or c == 'ト': out += 'tto'
		elif c == 'な' or c == 'ナ': out += 'nna'
		elif c == 'に' or c == 'ニ': out += 'nni'
		elif c == 'ぬ' or c == 'ヌ': out += 'nnu'
		elif c == 'ね' or c == 'ネ': out += 'nne'
		elif c == 'の' or c == 'ノ': out += 'nno'
		elif c == 'は' or c == 'ハ': out += 'hha'
		elif c == 'ひ' or c == 'ヒ': out += 'hhi'
		elif c == 'ふ' or c == 'フ': out += 'ffu'
		elif c == 'へ' or c == 'ヘ': out += 'hhe'
		elif c == 'ほ' or c == 'ホ': out += 'hho'
		elif c == 'ま' or c == 'マ': out += 'mma'
		elif c == 'み' or c == 'ミ': out += 'mmi'
		elif c == 'む' or c == 'ム': out += 'mmu'
		elif c == 'め' or c == 'メ': out += 'mme'
		elif c == 'も' or c == 'モ': out += 'mmo'
		elif c == 'や' or c == 'ヤ': out += 'yya'
		elif c == 'ゆ' or c == 'ユ': out += 'yyu'
		elif c == 'よ' or c == 'ヨ': out += 'yyo'
		elif c == 'ら' or c == 'ラ': out += 'rra'
		elif c == 'り' or c == 'リ': out += 'rri'
		elif c == 'る' or c == 'ル': out += 'rru'
		elif c == 'れ' or c == 'レ': out += 'rre'
		elif c == 'ろ' or c == 'ロ': out += 'rro'
		elif c == 'わ' or c == 'ワ': out += 'wwa'
		elif c == 'を' or c == 'ヲ': out += 'wwo'
		elif c == 'ん' or c == 'ン': out += 'nn'
		elif c == 'が' or c == 'ガ': out += 'kka'
		elif c == 'ぎ' or c == 'ギ': out += 'ggi'
		elif c == 'ぐ' or c == 'グ': out += 'ggu'
		elif c == 'げ' or c == 'ゲ': out += 'gge'
		elif c == 'ご' or c == 'ゴ': out += 'ggo'
		elif c == 'ざ' or c == 'ザ': out += 'zza'
		elif c == 'じ' or c == 'ジ': out += 'jji'
		elif c == 'ず' or c == 'ズ': out += 'zzu'
		elif c == 'ぜ' or c == 'ゼ': out += 'zze'
		elif c == 'ぞ' or c == 'ゾ': out += 'zzo'
		elif c == 'だ' or c == 'ダ': out += 'dda'
		elif c == 'ぢ' or c == 'ヂ': out += 'jji'
		elif c == 'づ' or c == 'ヅ': out += 'zzu'
		elif c == 'で' or c == 'デ': out += 'dde'
		elif c == 'ど' or c == 'ド': out += 'ddo'
		elif c == 'ば' or c == 'バ': out += 'bba'
		elif c == 'び' or c == 'ビ': out += 'bbi'
		elif c == 'ぶ' or c == 'ブ': out += 'bbu'
		elif c == 'べ' or c == 'ベ': out += 'bbe'
		elif c == 'ぼ' or c == 'ボ': out += 'bbo'
		elif c == 'ぱ' or c == 'パ': out += 'ppa'
		elif c == 'ぴ' or c == 'ピ': out += 'ppi'
		elif c == 'ぷ' or c == 'プ': out += 'ppu'
		elif c == 'ぺ' or c == 'ペ': out += 'ppe'
		elif c == 'ぽ' or c == 'ポ': out += 'ppo'
		elif c == 'きゃ' or c == 'キャ': out += 'kkya'
		elif c == 'きゅ' or c == 'キュ': out += 'kkyu'
		elif c == 'きょ' or c == 'キョ': out += 'kkyo'
		elif c == 'ぎゃ' or c == 'ギャ': out += 'ggya'
		elif c == 'ぎゅ' or c == 'ギュ': out += 'ggyu'
		elif c == 'ぎょ' or c == 'ギョ': out += 'ggyo'
		elif c == 'しゃ' or c == 'シャ': out += 'ssha'
		elif c == 'しゅ' or c == 'シュ': out += 'sshu'
		elif c == 'しょ' or c == 'ショ': out += 'ssho'
		elif c == 'じゃ' or c == 'ジャ': out += 'jja'
		elif c == 'じゅ' or c == 'ジュ': out += 'jju'
		elif c == 'じょ' or c == 'ジョ': out += 'jjo'
		elif c == 'ちゃ' or c == 'チャ': out += 'ccha'
		elif c == 'ちゅ' or c == 'チュ': out += 'cchu'
		elif c == 'ちょ' or c == 'チョ': out += 'ccho'
		elif c == 'にゃ' or c == 'ニャ': out += 'nnya'
		elif c == 'にゅ' or c == 'ニュ': out += 'nnyu'
		elif c == 'にょ' or c == 'ニョ': out += 'nnyo'
		elif c == 'ひゃ' or c == 'ヒャ': out += 'hhya'
		elif c == 'ひゅ' or c == 'ヒュ': out += 'hhyu'
		elif c == 'ひょ' or c == 'ヒョ': out += 'hhyo'
		elif c == 'びゃ' or c == 'ビャ': out += 'bbya'
		elif c == 'びゅ' or c == 'ビュ': out += 'bbyu'
		elif c == 'びょ' or c == 'ビョ': out += 'bbyo'
		elif c == 'みゃ' or c == 'ミャ': out += 'mmya'
		elif c == 'みゅ' or c == 'ミュ': out += 'mmyu'
		elif c == 'みょ' or c == 'ミョ': out += 'mmyo'
		elif c == 'ぴゃ' or c == 'ピャ': out += 'ppya'
		elif c == 'ぴゅ' or c == 'ピュ': out += 'ppyu'
		elif c == 'ぴょ' or c == 'ピョ': out += 'ppyo'
		elif c == 'りゃ' or c == 'リャ': out += 'rrya'
		elif c == 'りゅ' or c == 'リュ': out += 'rryu'
		elif c == 'りょ' or c == 'リョ': out += 'rryo'
		else: out += c
		chisaiTsu = False
	else:
		if c == 'あ' or c == 'ア': out += 'a' 
		elif c == 'い' or c == 'イ': out += 'i'
		elif c == 'う' or c == 'ウ': out += 'u'
		elif c == 'え' or c == 'エ': out += 'e'
		elif c == 'お' or c == 'オ': out += 'o'
		elif c == 'か' or c == 'カ': out += 'ka'
		elif c == 'き' or c == 'キ': out += 'ki'
		elif c == 'く' or c == 'ク': out += 'ku'
		elif c == 'け' or c == 'ケ': out += 'ke'
		elif c == 'こ' or c == 'コ': out += 'ko'
		elif c == 'さ' or c == 'サ': out += 'sa'
		elif c == 'し' or c == 'シ': out += 'shi'
		elif c == 'す' or c == 'ス': out += 'su'
		elif c == 'せ' or c == 'セ': out += 'se'
		elif c == 'そ' or c == 'ソ': out += 'so'
		elif c == 'た' or c == 'タ': out += 'ta'
		elif c == 'ち' or c == 'チ': out += 'chi'
		elif c == 'つ' or c == 'ツ': out += 'tsu'
		elif c == 'て' or c == 'テ': out += 'te'
		elif c == 'と' or c == 'ト': out += 'to'
		elif c == 'な' or c == 'ナ': out += 'na'
		elif c == 'に' or c == 'ニ': out += 'ni'
		elif c == 'ぬ' or c == 'ヌ': out += 'nu'
		elif c == 'ね' or c == 'ネ': out += 'ne'
		elif c == 'の' or c == 'ノ': out += 'no'
		elif c == 'は' or c == 'ハ': out += 'ha'
		elif c == 'ひ' or c == 'ヒ': out += 'hi'
		elif c == 'ふ' or c == 'フ': out += 'fu'
		elif c == 'へ' or c == 'ヘ': out += 'he'
		elif c == 'ほ' or c == 'ホ': out += 'ho'
		elif c == 'ま' or c == 'マ': out += 'ma'
		elif c == 'み' or c == 'ミ': out += 'mi'
		elif c == 'む' or c == 'ム': out += 'mu'
		elif c == 'め' or c == 'メ': out += 'me'
		elif c == 'も' or c == 'モ': out += 'mo'
		elif c == 'や' or c == 'ヤ': out += 'ya'
		elif c == 'ゆ' or c == 'ユ': out += 'yu'
		elif c == 'よ' or c == 'ヨ': out += 'yo'
		elif c == 'ら' or c == 'ラ': out += 'ra'
		elif c == 'り' or c == 'リ': out += 'ri'
		elif c == 'る' or c == 'ル': out += 'ru'
		elif c == 'れ' or c == 'レ': out += 're'
		elif c == 'ろ' or c == 'ロ': out += 'ro'
		elif c == 'わ' or c == 'ワ': out += 'wa'
		elif c == 'を' or c == 'ヲ': out += 'wo'
		elif c == 'ん' or c == 'ン': out += 'n'
		elif c == 'が' or c == 'ガ': out += 'ka'
		elif c == 'ぎ' or c == 'ギ': out += 'gi'
		elif c == 'ぐ' or c == 'グ': out += 'gu'
		elif c == 'げ' or c == 'ゲ': out += 'ge'
		elif c == 'ご' or c == 'ゴ': out += 'go'
		elif c == 'ざ' or c == 'ザ': out += 'za'
		elif c == 'じ' or c == 'ジ': out += 'ji'
		elif c == 'ず' or c == 'ズ': out += 'zu'
		elif c == 'ぜ' or c == 'ゼ': out += 'ze'
		elif c == 'ぞ' or c == 'ゾ': out += 'zo'
		elif c == 'だ' or c == 'ダ': out += 'da'
		elif c == 'ぢ' or c == 'ヂ': out += 'ji'
		elif c == 'づ' or c == 'ヅ': out += 'zu'
		elif c == 'で' or c == 'デ': out += 'de'
		elif c == 'ど' or c == 'ド': out += 'do'
		elif c == 'ば' or c == 'バ': out += 'ba'
		elif c == 'び' or c == 'ビ': out += 'bi'
		elif c == 'ぶ' or c == 'ブ': out += 'bu'
		elif c == 'べ' or c == 'ベ': out += 'be'
		elif c == 'ぼ' or c == 'ボ': out += 'bo'
		elif c == 'ぱ' or c == 'パ': out += 'pa'
		elif c == 'ぴ' or c == 'ピ': out += 'pi'
		elif c == 'ぷ' or c == 'プ': out += 'pu'
		elif c == 'ぺ' or c == 'ペ': out += 'pe'
		elif c == 'ぽ' or c == 'ポ': out += 'po'
		elif c == 'きゃ' or c == 'キャ': out += 'kya'
		elif c == 'きゅ' or c == 'キュ': out += 'kyu'
		elif c == 'きょ' or c == 'キョ': out += 'kyo'
		elif c == 'ぎゃ' or c == 'ギャ': out += 'gya'
		elif c == 'ぎゅ' or c == 'ギュ': out += 'gyu'
		elif c == 'ぎょ' or c == 'ギョ': out += 'gyo'
		elif c == 'しゃ' or c == 'シャ': out += 'sha'
		elif c == 'しゅ' or c == 'シュ': out += 'shu'
		elif c == 'しょ' or c == 'ショ': out += 'sho'
		elif c == 'じゃ' or c == 'ジャ': out += 'ja'
		elif c == 'じゅ' or c == 'ジュ': out += 'ju'
		elif c == 'じょ' or c == 'ジョ': out += 'jo'
		elif c == 'ちゃ' or c == 'チャ': out += 'cha'
		elif c == 'ちゅ' or c == 'チュ': out += 'chu'
		elif c == 'ちょ' or c == 'チョ': out += 'cho'
		elif c == 'にゃ' or c == 'ニャ': out += 'nya'
		elif c == 'にゅ' or c == 'ニュ': out += 'nyu'
		elif c == 'にょ' or c == 'ニョ': out += 'nyo'
		elif c == 'ひゃ' or c == 'ヒャ': out += 'hya'
		elif c == 'ひゅ' or c == 'ヒュ': out += 'hyu'
		elif c == 'ひょ' or c == 'ヒョ': out += 'hyo'
		elif c == 'びゃ' or c == 'ビャ': out += 'bya'
		elif c == 'びゅ' or c == 'ビュ': out += 'byu'
		elif c == 'びょ' or c == 'ビョ': out += 'byo'
		elif c == 'みゃ' or c == 'ミャ': out += 'mya'
		elif c == 'みゅ' or c == 'ミュ': out += 'myu'
		elif c == 'みょ' or c == 'ミョ': out += 'myo'
		elif c == 'ぴゃ' or c == 'ピャ': out += 'pya'
		elif c == 'ぴゅ' or c == 'ピュ': out += 'pyu'
		elif c == 'ぴょ' or c == 'ピョ': out += 'pyo'
		elif c == 'りゃ' or c == 'リャ': out += 'rya'
		elif c == 'りゅ' or c == 'リュ': out += 'ryu'
		elif c == 'りょ' or c == 'リョ': out += 'ryo'
		else: out += c
print(out)
