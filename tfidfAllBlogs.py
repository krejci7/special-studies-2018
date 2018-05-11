from tfidf3 import tfidf
import json

# just wrong: transgenders
#
# dated: transsexual, transgendered, male, female, "born male", "born female", natal, sex change, transvestite, tgirl, tgirls,
# transform, transgenderism, "genetic male", "genetic female"

# protogay, prehomosexual, homosexual
#
# modern: transgender, trans, nonbinary, genderqueer, AMAB, DMAB, AFAB, DFAB, CAMAB, CAFAB, SRS, GRS, "assigned male", "assigned female",
# queer, transition, transitioning, legible, privilege
#
vocab = ["transgender", "trans", "nonbinary", "genderqueer", "AMAB", "DMAB", "AFAB", "DFAB", "CAMAB", "CAFAB", "SRS", "GRS", "assign male",
"assign female", "queer", "transition", "legible", "privilege", "GNC", "gender nonconforming","gay","transgenders", "transsexual",
"transgendered","bear male","bear female","natal male", "natal female","sex change","transvestite","tgirl","tgirls","transform",
"transgenderism","genetic male","genetic female","protogay","prehomosexual","homosexual", "become man", "become woman","biological male",
"biological female","NB","enby", "transmasculine","transfeminine", "mutilate","cis","autogynephile","autogynephiles","autogynephilia",
"autogynephilic"]


file = "FullBlogs/AllBlogs.txt"
with open(file) as myfile:
    final = json.loads(myfile.read())
del final['6']
del final['9']
file = "FullBlogs/indices.txt"
with open(file) as myfile:
    i = json.loads(myfile.read())

tf = tfidf(final, maxfeatures=5000, vocab=vocab)
# print(tf.most_common_all(10))

# print("Most similar: ", tf.most_similar()[0],tf.most_similar()[1])
# print("Least similar: ", tf.least_similar()[0],tf.least_similar()[1])

# print(tf.cos_sim_all())

tf.most_common(0)
tf.most_common(1)
tf.most_common(2)
tf.most_common(3)
tf.most_common(4)
tf.most_common(5)
tf.most_common(6)
tf.most_common(7)
tf.most_common(8)

tf.heat_map()

# print("total words: ", tf.total_words())



"""
blog characterizations
BeardedGQ: nonbinary transfem with a beard, they/them, casual but not Super casual voice, modern terminology, life updates
BornWrong: early 20s detransitioned butch lesbian, highly political, critical, gendercrit terminology
CFlourish: middle-aged? trans woman, slightly dated language, highly political
DTando: cis therapist, kid-focused, positive, mostly modern langauge, modern ideals
genderkid: Argentinian trans man / maybe genderqueer, often transition/testosterone-focused, modern language
HerDog: border of trans and butch, middle-aged, they/them, focused on life updates, modern language
HMcK: "T-Girl", life updates, dated language
JanitorQ: genderqueer janitor, focused on life updates with some transition/testosterone, modern language
RadQ: zie/hir, VERY liberal/modern language, highly political
RmyR: cis mom of a "gender creative son", "gender expansive", cis mom language, focused on life updates
TransBlog: transfem, "the slippery slope", dated, political, gendercrit

expected similarities
group 1 ("gendercrit"): BornWrong, TransBlog
group 2 (real life): BeardedGQ, HerDog, JanitorQ, RmyR, HMcK
group 3 (transition): genderkid, JanitorQ
group 4 (politics): BornWrong, CFlourish, 
group 5 (outdated): BornWrong, TransBlog, CFlourish, HMcK
group 6 (modern and trans): BeardedGQ, genderkid, HerDog, JanitorQ, RadQ
group 7 (modern and not trans): DTando, RmyR
group 8 (modern): BeardedGQ, genderkid, HerDog, JanitorQ, RadQ, DTando, RmyR

expected differences
group 1 vs. group 8
group 2 vs. group 4
group 3 vs. group 4 (and group 2, less so)
"""


"""
{"BeardedGQ": 0,
"BornWrong": 1,
"CFlourish": 2,
"DTando": 3,
"genderkid": 4,
"HerDog": 5,
"HMcK": 6,
"JanitorQ": 7,
"RadQ": 8,
"RmyR": 9,
"TransBlog": 10}
"""



# similarity by word
# spider plot (or bar chart)