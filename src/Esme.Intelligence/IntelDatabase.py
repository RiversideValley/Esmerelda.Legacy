from Flux import stx

stx.region("code")

class intel(object):
    def __init__(data, name, bundle, hash, desc, answerIsBool, question, answer):
        data.name = name
        data.bundle = bundle
        data.hash = hash
        data.desc = desc
        data.answerIsBool = answerIsBool
        data.question = question
        data.answer = answer

stx.region("data")

testEntry = intel("Test", "Esme.Intelligence.Data.testEntry", "28c5a48b66421c96c11e836e46e4aacd", "Test Entry for Esmerelda", True, "Is the test true", True)