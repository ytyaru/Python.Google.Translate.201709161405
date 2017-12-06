from WebApi.Google.Translate import Translator
sentence = "My name is Ann. "
print('翻訳前:', sentence)
print('翻訳後:', Translator.Translate(sentence, 'en', 'ja'))
