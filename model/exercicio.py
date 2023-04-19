
# classe para tratar os exercicios
class Exercicio:
    def __init__(self,name, url, category, nivel, type, division, required):
        self.name = name
        self.url = url
        self.category = category
        self.nivel = nivel
        self.type = type
        self.division = division
        self.required = required

        
    def getAllExercicios():
        exercises = [
        {'name': 'Knee Push Ups (de joelho)', 'url': 'https://cdn.w600.comps.canstockphoto.com.br/trabalhando-dela-joelho-femininas-vetor-clip-arte_csp89802369.jpg', 'category': 'Push', 'nivel': 0, 'type': 'Horizontal', 'division': 'Flexão (Push Ups) - Horizontal', 'required': '' },
        {'name': 'Flexão Padrão', 'url': 'https://aprovataf.com.br/wp-content/uploads/2016/04/Flex%C3%A3o-de-bra%C3%A7o-no-solo-AprovaTAF.jpg', 'category': 'Push', 'nivel': 1, 'type': 'Horizontal', 'division': 'Flexão (Push Ups) - Horizontal', 'default': 'true', 'required': '' },
        { 'name': 'Diamond Push Ups', 'url': 'https://weighttraining.guide/wp-content/uploads/2017/07/diamond-push-up-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4', 'category': 'Push', 'nivel': 2, 'type': 'Horizontal', 'division': 'Flexão (Push Ups) - Horizontal', 'required': '' },
        { 'name': 'Archer Push Ups ', 'url': 'https://images.squarespace-cdn.com/content/v1/5db20c73f80047725e83b73c/1605191028463-69TG5D2LHACZDGBUSVOX/service_1589888550_3778.jpg', 'category': 'Push', 'nivel': 3, 'type': 'Horizontal', 'division': 'Flexão (Push Ups) - Horizontal', 'required': '' },
        { 'name': 'Rings Push Ups', 'url': 'https://www.fitstream.com/images/ring-training/exercises/ring-push-up.png?w=80&h=80', 'category': 'Push', 'nivel': 4, 'type': 'Horizontal', 'division': 'Flexão (Push Ups) - Horizontal', 'required': 'argolas' },
        { 'name': 'One Arm Push Ups Elevada', 'url': 'https://static.strengthlevel.com/images/illustrations/one-arm-push-ups-1000x1000.jpg', 'category': 'Push', 'nivel': 5, 'type': 'Horizontal', 'division': 'Flexão (Push Ups) - Horizontal', 'required': '' },
        { 'name': 'One Arm Push Ups/Tuck Planche', 'url': 'https://post.healthline.com/wp-content/uploads/2019/07/Man-Exercising-1200x628-facebook.jpg', 'category': 'Push', 'nivel': 6, 'type': 'Horizontal', 'division': 'Flexão (Push Ups) - Horizontal', 'required': '' },
        { 'name': 'Bench Dips (Dips no banco)', 'url': 'https://media.istockphoto.com/id/1277965681/pt/vetorial/bench-triceps-dips-female-exercise-guide-colorful-illustration.jpg?s=170667a&w=0&k=20&c=rys1gAWR29rv2zQL21jzAxKAmUhOaobuUjYkKQkOqj8=', 'category': 'Push', 'nivel': 0, 'type': 'Vertical', 'division': 'Dips - Vertical', 'required': '' },
        { 'name': 'Dips com ajuda ou elastico', 'url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Dips.png/330px-Dips.png', 'category': 'Push', 'nivel': 1, 'type': 'Vertical', 'division': 'Dips - Vertical', 'required': ['paralelas', 'superband'] },
        { 'name': 'Dips negativo', 'url': 'https://julienquaglierini.com/wp-content/uploads/2018/08/dips-768x432.jpg.webp', 'category': 'Push', 'nivel': 1, 'type': 'Vertical', 'division': 'Dips - Vertical', 'required': 'paralelas' },
        
        { 'name': 'Dips na paralela', 'url': 'https://static.netshoes.com.br/produtos/barra-paralela-dip-de-parede-calistenia-(parafusos-e-buchas-plasticas)/06/06O-0003-006/06O-0003-006_zoom3.jpg?ts=1601643646', 'category': 'Push', 'nivel': [2, 3], 'type': 'Vertical', 'division': 'Dips - Vertical', 'default': 'true', 'required': 'paralelas' },
        { 'name': 'Dips em L-sit', 'url': 'https://www.shutterstock.com/image-vector/male-athlete-silhouette-doing-calisthenics-600w-1348704965.jpg', 'category': 'Push', 'nivel': 4, 'type': 'Vertical', 'division': 'Dips - Vertical', 'required': ['paralelas', 'argolas'] },
        { 'name': 'Dips a 45º (inclinado para frente)', 'url': '../img/Dips45ºpng.png', 'category': 'Push', 'nivel': 4, 'type': 'Vertical', 'division': 'Dips - Vertical', 'required': 'paralelas' },
        { 'name': 'Tuck Planche Push Ups', 'url': 'https://qph.cf2.quoracdn.net/main-qimg-1782c86f06ca832b93dc8ae85ed637ae', 'category': 'Push', 'nivel': 6, 'type': 'Vertical', 'division': 'Dips - Vertical', 'required': '' },
        { 'name': 'Rings Suppor Hold ', 'url': 'https://bodydojo.com/wp-content/uploads/2018/06/RTO-support-400x300.jpg', 'category': 'Push', 'nivel': 1, 'type': 'Vertical', 'division': 'Dips na Argola - Vertical', 'required': 'argolas' },
        { 'name': 'Rings Suppor Hold Supinado', 'url': 'https://s3.amazonaws.com/prod.skimble/assets/832102/image_iphone.jpg', 'category': 'Push', 'nivel': 2, 'type': 'Vertical', 'division': 'Dips na Argola - Vertical', 'required': 'argolas' },
        { 'name': 'Ring Dips Negativo', 'url': 'https://img.myloview.com.br/fotomurais/woman-doing-gymnastic-ring-dips-exercise-flat-vector-illustration-isolated-on-white-background-700-277885449.jpg', 'category': 'Push', 'nivel': 3, 'type': 'Vertical', 'division': 'Dips na Argola - Vertical', 'required': 'argolas' },
        { 'name': 'Ring Dips', 'url': 'https://previews.123rf.com/images/lioputra/lioputra2011/lioputra201100076/158973747-gymnastic-ring-dips-exercise-flat-vector-illustration-isolated-on-white-background-workout.jpg', 'category': 'Push', 'nivel': 4, 'type': 'Vertical', 'division': 'Dips na Argola - Vertical', 'required': 'argolas' },
        { 'name': 'Dips em L-sit/Buldarian Dips', 'url': 'https://cdn.vectorstock.com/i/1000x1000/05/62/man-doing-chair-bench-tricep-dips-exercise-vector-42870562.webp', 'category': 'Push', 'nivel': 5, 'type': 'Vertical', 'division': 'Dips na Argola - Vertical', 'required': '' },
        { 'name': 'Ring Dips Supinado', 'url': 'https://www.shutterstock.com/image-vector/sporty-man-doing-ring-dips-600w-1360756589.jpg', 'category': 'Push', 'nivel': 6, 'type': 'Vertical', 'division': 'Dips na Argola - Vertical', 'required': 'argolas' },
        { 'name': 'Dips com ajuda', 'url': 'https://thumbs.dreamstime.com/z/ilustra%C3%A7%C3%A3o-de-vetor-for%C3%A7a-exerc%C3%ADcio-barra-dip-do-varejo-com-fundo-branco-vetorial-215590449.jpg', 'category': 'Push', 'nivel': 1, 'type': 'Vertical', 'division': 'Weigthed Dips - Vertical', 'required': ' paralelas' },
        { 'name': 'Dips + 20% do seu peso', 'url': 'https://ginasiovirtual.com/wp-content/uploads/2021/06/fundos-com-peso.jpg', 'category': 'Push', 'nivel': 4, 'type': 'Vertical', 'division': 'Weigthed Dips - Vertical', 'required': 'paralelas' },
        { 'name': 'Dips + 38% do seu peso', 'url': 'https://ginasiovirtual.com/wp-content/uploads/2021/06/fundos-com-peso.jpg', 'category': 'Push', 'nivel': 5, 'type': 'Vertical', 'division': 'Weigthed Dips - Vertical', 'required': 'paralelas' },
        { 'name': 'Dips + 55% do seu peso ', 'url': 'https://ginasiovirtual.com/wp-content/uploads/2021/06/fundos-com-peso.jpg', 'category': 'Push', 'nivel': 6, 'type': 'Vertical', 'division': 'Weigthed Dips - Vertical', 'required': 'paralelas' },
        { 'name': 'Pike Push Ups', 'url': 'https://qph.cf2.quoracdn.net/main-qimg-47c44c047bbb8118ed02ff236da07841-lq', 'category': 'Push', 'nivel': 1, 'type': 'Vertical', 'division': 'Flexão na Parada de Mãos - Vertical', 'required': '' },
        { 'name': 'Elevated Pike PU', 'url': 'https://b1494239.smushcdn.com/1494239/wp-content/uploads/2013/12/pike-push-up-advanced-e1438882945766.jpg?lossy=0&strip=1&webp=1', 'category': 'Push', 'nivel': 2, 'type': 'Vertical', 'division': 'Flexão na Parada de Mãos - Vertical', 'required': '' },
        { 'name': 'HSPU Negativo com kick | sem kick', 'url': 'https://www.getpersonalgrowth.com/images/posts/8a57dd56ac409541f34d096ff1f903f4-0.jpg', 'category': 'Push', 'nivel': 3, 'type': 'Vertical', 'division': 'Flexão na Parada de Mãos - Vertical', 'required': '' },
        { 'name': 'Wall HSPU (Handstand Push Ups)', 'url': 'https://images.contentstack.io/v3/assets/blt45c082eaf9747747/blt2c3e741ea4156df4/5dee7c59d03adf37d49cc286/Florian_HSPU_ES_HEAD.jpg?format=pjpg&auto=webp&quality=76&width=716', 'category': 'Push', 'nivel': 4, 'type': 'Vertical', 'division': 'Flexão na Parada de Mãos - Vertical', 'required': '' },
        { 'name': 'Wall HSPU c/ Paralela de frente | de costas', 'url': 'https://elemento.ag/blog/wp-content/uploads/2022/02/image6.jpg', 'category': 'Push', 'nivel': 5, 'type': 'Vertical', 'division': 'Flexão na Parada de Mãos - Vertical', 'required': '' },
        { 'name': 'HSPU Livre', 'url': 'https://http2.mlstatic.com/D_NQ_NP_2X_813656-MLB46427391074_062021-F.webp', 'category': 'Push', 'nivel': 6, 'type': 'Vertical', 'division': 'Flexão na Parada de Mãos - Vertical', 'required': '' },
        { 'name': 'Negativas de Remada', 'url': 'https://treinomestre.com.br/wp-content/uploads/2021/11/remada-articulada.jpg', 'category': 'Pull', 'nivel': 1, 'type': 'Horizontal', 'division': ' Rows/Barra Australiana - Horizontal', 'required': ['argolas', 'paralelas', 'barraFixa', 'trx'] },
        { 'name': 'Rows/Barra Australiana', 'url': 'https://www.sport.es/labolsadelcorredor/wp-content/uploads/2018/05/Australian-pull-up.jpg', 'category': 'Pull', 'nivel': 2, 'type': 'Horizontal', 'division': ' Rows/Barra Australiana - Horizontal', 'default': 'true', 'required': ['argolas', 'paralelas', 'barraFixa', 'trx'] },
        { 'name': 'Wide Rows (pegada aberta)', 'url': 'https://www.spotebi.com/wp-content/uploads/2015/04/wide-row-exercise-illustration.jpg', 'category': 'Pull', 'nivel': 3, 'type': 'Horizontal', 'division': ' Rows/Barra Australiana - Horizontal', 'required': ['argolas', 'paralelas', 'barraFixa', 'trx'] },
        { 'name': 'Archer Rows Braços Dobrados ou Alta', 'url': 'https://cdn.vectorstock.com/i/1000x1000/36/80/woman-doing-upper-back-exercise-archer-with-long-r-vector-43113680.webp', 'category': 'Pull', 'nivel': 4, 'type': 'Horizontal', 'division': ' Rows/Barra Australiana - Horizontal', 'required': '' },
        { 'name': 'Archer Rows (braço esticado)/Tuck Front Lever', 'url': 'https://cdn.vectorstock.com/i/1000x1000/36/80/woman-doing-upper-back-exercise-archer-with-long-r-vector-43113680.webp', 'category': 'Pull', 'nivel': 5, 'type': 'Horizontal', 'division': ' Rows/Barra Australiana - Horizontal', 'required': ['argolas', 'paralelas', 'barraFixa', 'trx'] },
        { 'name': 'Straddle One Arm Rows', 'url': 'https://www.shutterstock.com/image-vector/man-doing-single-arm-bent-600w-2101536073.jpg', 'category': 'Pull', 'nivel': 6, 'type': 'Horizontal', 'division': ' Rows/Barra Australiana - Horizontal', 'required': ['argolas', 'paralelas', 'barraFixa', 'trx'] },
        { 'name': 'Pull Ups com ajuda ou elastico', 'url': 'https://network.grupoabril.com.br/wp-content/uploads/sites/2/2017/01/xxxx.jpg?quality=85&strip=all&w=1024', 'category': 'Pull', 'nivel': 0, 'type': 'Vertical', 'division': 'Barra Fixa (Pull Ups) - Vertical', 'required': ['barraFixa', 'superband'] },
        { 'name': 'Pull Ups negativo', 'url': 'https://www.fitstream.com/images/bodyweight-training/bodyweight-exercises/negative-pull-up-main.png', 'category': 'Pull', 'nivel': 2, 'type': 'Vertical', 'division': 'Barra Fixa (Pull Ups) - Vertical', 'required': 'barraFixa' },
        { 'name': 'Pull Ups em L-sit', 'url': 'https://i.pinimg.com/564x/f3/b2/eb/f3b2eb20fc9472333072dab45e4140a6.jpg', 'category': 'Pull', 'nivel': 4, 'type': 'Vertical', 'division': 'Barra Fixa (Pull Ups) - Vertical', 'required': 'barraFixa' },
        { 'name': 'Wide Pull Ups (pegada aberta)', 'url': 'https://images.squarespace-cdn.com/content/v1/57efdb4cd482e918dc2a900f/1658358689971-JZXGL3SS7MY5ES2S9VVT/extra+wide+pull+up+grip.JPG?format=500w', 'category': 'Pull', 'nivel': 5, 'type': 'Vertical', 'division': 'Barra Fixa (Pull Ups) - Vertical', 'required': 'barraFixa' },
        { 'name': 'Wide Pull Ups em L-sit', 'url': 'https://www.fitliferegime.com/wp-content/uploads/2023/01/Muscle-Worked-During-Pull-Ups-1024x683.webp?ezimgfmt=ng:webp/ngcb1', 'category': 'Pull', 'nivel': 6, 'type': 'Vertical', 'division': 'Barra Fixa (Pull Ups) - Vertical', 'required': 'barraFixa' },
        { 'name': 'Archer Pull ups', 'url': 'https://kengurupro.eu/wp-content/uploads/2020/10/k-005-1-1.jpg', 'category': 'Pull', 'nivel': 6, 'type': 'Vertical', 'division': 'One Arm Pull Ups (um braço) - Vertical', 'required': 'barraFixa' },
        { 'name': 'Pull Ups com ajuda', 'url': 'https://network.grupoabril.com.br/wp-content/uploads/sites/2/2017/01/xxxx.jpg?quality=85&strip=all&w=1024', 'category': 'Pull', 'nivel': 1, 'type': 'Vertical', 'division': 'Weigthed Pull Ups - Vertical', 'required': 'barraFixa' },
        { 'name': 'Pull Ups', 'url': 'http://2.bp.blogspot.com/-kKolopOtBl8/UDvUdp8cDTI/AAAAAAAABw8/KwV1AzFxPsE/s400/FITNESS_proradicalskate.jpg', 'category': 'Pull', 'nivel': 3, 'type': 'Vertical', 'division': 'Weigthed Pull Ups - Vertical', 'required': 'barraFixa' },
        { 'name': 'Pull Ups +18% seu peso', 'url': 'https://st4.depositphotos.com/13768208/40092/i/450/depositphotos_400928346-stock-photo-cross-fit-seminar-staff-member.jpg', 'category': 'Pull', 'nivel': 4, 'type': 'Vertical', 'division': 'Weigthed Pull Ups - Vertical', 'required': 'barraFixa' },
        { 'name': 'Pull Ups +35% seu peso', 'url': 'https://st4.depositphotos.com/13768208/40092/i/450/depositphotos_400928346-stock-photo-cross-fit-seminar-staff-member.jpg', 'category': 'Pull', 'nivel': 5, 'type': 'Vertical', 'division': 'Weigthed Pull Ups - Vertical', 'required': 'barraFixa' },
        { 'name': 'Pull Ups +50% seu peso', 'url': 'https://st4.depositphotos.com/13768208/40092/i/450/depositphotos_400928346-stock-photo-cross-fit-seminar-staff-member.jpg', 'category': 'Pull', 'nivel': 6, 'type': 'Vertical', 'division': 'Weigthed Pull Ups - Vertical', 'required': 'barraFixa' },
        { 'name': 'Kipping Pull-ups', 'url': 'https://i.ytimg.com/vi_webp/AyPTCEXTjOo/maxresdefault.webp', 'category': 'Pull', 'nivel': 2, 'type': 'Vertical', 'division': 'Pull Ups Explosivos - Vertical', 'required': 'barraFixa' },
        { 'name': 'Pull-ups', 'url': 'http://2.bp.blogspot.com/-kKolopOtBl8/UDvUdp8cDTI/AAAAAAAABw8/KwV1AzFxPsE/s400/FITNESS_proradicalskate.jpg', 'category': 'Pull', 'nivel': 3, 'type': 'Vertical', 'division': 'Pull Ups Explosivos - Vertical', 'required': 'barraFixa' },
        { 'name': 'Kipping Pull-ups com Palma', 'url': 'https://i.ytimg.com/vi_webp/AyPTCEXTjOo/maxresdefault.webp', 'category': 'Pull', 'nivel': 4, 'type': 'Vertical', 'division': 'Pull Ups Explosivos - Vertical', 'required': 'barraFixa' },
        { 'name': 'Pull-ups com Palma sem Kipping', 'url': 'https://doutorjairo.uol.com.br/media/uploads/istock-923748448.jpg', 'category': 'Pull', 'nivel': 5, 'type': 'Vertical', 'division': 'Pull Ups Explosivos - Vertical', 'required': 'barraFixa' },
        { 'name': 'L-sit Pull-ups com Palma', 'url': 'https://i.pinimg.com/564x/f3/b2/eb/f3b2eb20fc9472333072dab45e4140a6.jpg', 'category': 'Pull', 'nivel': 6, 'type': 'Vertical', 'division': 'Pull Ups Explosivos - Vertical', 'required': 'barraFixa' },
        { 'name': 'Squat 45º', 'url': 'https://static.tuasaude.com/media/article/3k/ru/6-exercicios-de-agachamento-para-gluteos_9131_l.jpg', 'category': 'Legs', 'nivel': 1, 'type': 'Parte da frente', 'division': 'Squat (Push) - Parte da frente', 'required': '' },
        { 'name': 'Full Squat (descer tudo)', 'url': 'https://static.vecteezy.com/ti/vetor-gratis/p2/8635575-mulher-fazendo-peso-corporal-agachamento-exercicio-plano-ilustracao-isolado-em-fundo-branco-vetor.jpg', 'category': 'Legs', 'nivel': 2, 'type': 'Parte da frente', 'division': 'Squat (Push) - Parte da frente', 'default': 'true', 'required': '' },
        { 'name': 'Side to Side Squat', 'url': 'https://www.spotebi.com/wp-content/uploads/2015/02/side-to-side-squats-exercise-illustration.jpg', 'category': 'Legs', 'nivel': 3, 'type': 'Parte da frente', 'division': 'Squat (Push) - Parte da frente', 'required': '' },
        { 'name': 'Pistol', 'url': 'https://www.spotebi.com/wp-content/uploads/2015/05/pistol-squat-exercise-illustration.jpg', 'category': 'Legs', 'nivel': 4, 'type': 'Parte da frente', 'division': 'Squat (Push) - Parte da frente', 'required': '' },
        { 'name': 'Pistol + 20% seu peso', 'url': 'https://horadotreino.com.br/wp-content/uploads/2013/12/agachamento-unilateral2.jpg', 'category': 'Legs', 'nivel': 5, 'type': 'Parte da frente', 'division': 'Squat (Push) - Parte da frente', 'required': '' },
        { 'name': 'Pistol + 35% seu peso', 'url': 'https://horadotreino.com.br/wp-content/uploads/2013/12/agachamento-unilateral2.jpg', 'category': 'Legs', 'nivel': 6, 'type': 'Parte da frente', 'division': 'Squat (Push) - Parte da frente', 'required': '' },
        { 'name': 'Hip Thruster', 'url': 'https://thumbs.dreamstime.com/z/mulher-fazendo-levantamentos-eleva%C3%A7%C3%A3o-da-bunda-exerc%C3%ADcio-de-pontes-que-exercem-uma-ilustra%C3%A7%C3%A3o-plana-do-vetor-isolada-em-fundo-236723402.jpg', 'category': 'Legs', 'nivel': 1, 'type': 'Parte de trás', 'division': 'Hip Thruster (Pull) - Parte de trás', 'default': 'true', 'required': '' },
        { 'name': 'Elevated Hip Thruster', 'url': 'https://doctorlib.info/sport/mens-health-body/mens-health-body.files/image024.jpg', 'category': 'Legs', 'nivel': 2, 'type': 'Parte de trás', 'division': 'Hip Thruster (Pull) - Parte de trás', 'required': '' },
        { 'name': 'One Leg Hip Thruster', 'url': 'https://cdn-0.weighttraining.guide/wp-content/uploads/2017/08/weighted-one-leg-hip-thrust-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4', 'category': 'Legs', 'nivel': 3, 'type': 'Parte de trás', 'division': 'Hip Thruster (Pull) - Parte de trás', 'required': '' },
        { 'name': 'Weighted Hip Thruster', 'url': 'https://cdn-0.weighttraining.guide/wp-content/uploads/2017/04/barbell-hip-thrust-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4', 'category': 'Legs', 'nivel': 4, 'type': 'Parte de trás', 'division': 'Hip Thruster (Pull) - Parte de trás', 'required': '' },
        { 'name': 'Stiff Unilateral', 'url': 'https://i.pinimg.com/564x/9d/6d/a9/9d6da9c12158ec52d1f660bf12fa490c.jpg', 'category': 'Legs', 'nivel': 1, 'type': 'Parte de trás', 'division': 'Nordic Curls (Pull) - Parte de trás', 'required': '' },
        { 'name': 'Flexão de Tronco', 'url': 'https://thumbs.dreamstime.com/z/exerc%C3%ADcio-da-aptid%C3%A3o-flex%C3%A3o-do-tronco-com-eleva%C3%A7%C3%A3o-da-pelve-que-encontra-se-no-assoalho-f%C3%AAmea-64591838.jpg', 'category': 'Legs', 'nivel': 2, 'type': 'Parte de trás', 'division': 'Nordic Curls (Pull) - Parte de trás', 'required': '' },
        { 'name': 'Nordic Cruls 45º', 'url': 'https://en.pimg.jp/076/410/785/1/76410785.jpg', 'category': 'Legs', 'nivel': 3, 'type': 'Parte de trás', 'division': 'Nordic Curls (Pull) - Parte de trás', 'required': '' },
        { 'name': 'Nordic Cruls Negativo', 'url': 'https://en.pimg.jp/076/410/785/1/76410785.jpg', 'category': 'Legs', 'nivel': 4, 'type': 'Parte de trás', 'division': 'Nordic Curls (Pull) - Parte de trás', 'required': '' },
        { 'name': 'Nordic Curls', 'url': 'https://hips.hearstapps.com/hmg-prod/images/screen-shot-2021-10-12-at-11-31-36-am-1634052723.png', 'category': 'Legs', 'nivel': 5, 'type': 'Parte de trás', 'division': 'Nordic Curls (Pull) - Parte de trás', 'required': '' },
        { 'name': 'Nordic Curls/braços para cima', 'url': 'https://hips.hearstapps.com/hmg-prod/images/screen-shot-2021-10-12-at-11-31-36-am-1634052723.png', 'category': 'Legs', 'nivel': 6, 'type': 'Parte de trás', 'division': 'Nordic Curls (Pull) - Parte de trás', 'required': '' },
        { 'name': 'Afundo/Bulgarian Squat', 'url': 'https://cdn-0.weighttraining.guide/wp-content/uploads/2021/10/Bulgarian-split-squat.png?ezimgfmt=ng%3Awebp%2Fngcb4', 'category': 'Legs', 'nivel': 2, 'type': 'Parte da frente', 'division': 'Shrimp Squat (Push) - Parte da frente', 'required': '' },
        { 'name': 'Shrimp com apoio no joelho', 'url': 'https://www.getstrong.fit/images/Shrimp-Squat.jpg?ezimgfmt=rs:620x347/rscb1/ng:webp/ngcb1', 'category': 'Legs', 'nivel': 3, 'type': 'Parte da frente', 'division': 'Shrimp Squat (Push) - Parte da frente', 'required': '' },
        { 'name': 'Shrimp com joelho ao chão', 'url': 'https://www.getstrong.fit/images/Shrimp-Squat.jpg?ezimgfmt=rs:620x347/rscb1/ng:webp/ngcb1', 'category': 'Legs', 'nivel': 4, 'type': 'Parte da frente', 'division': 'Shrimp Squat (Push) - Parte da frente', 'required': '' },
        { 'name': 'One Hand Shrimp', 'url': 'https://www.getstrong.fit/images/Shrimp-Squat.jpg?ezimgfmt=rs:620x347/rscb1/ng:webp/ngcb1', 'category': 'Legs', 'nivel': 5, 'type': 'Parte da frente', 'division': 'Shrimp Squat (Push) - Parte da frente', 'required': '' },
        { 'name': '2 Hands Shrimp', 'url': 'https://www.getstrong.fit/images/Shrimp-Squat.jpg?ezimgfmt=rs:620x347/rscb1/ng:webp/ngcb1', 'category': 'Legs', 'nivel': 6, 'type': 'Parte da frente', 'division': 'Shrimp Squat (Push) - Parte da frente', 'required': '' },
        { 'name': 'Reverse Nordic Curls | Smith Sissy', 'url': 'https://fitnessvolt.com/wp-content/uploads/2022/10/Reverse-Nordic-Curl-Guide-750x422.jpg', 'category': 'Legs', 'nivel': 2, 'type': 'Parte da frente', 'division': 'Shrimp Squat (Push) - Parte da frente', 'required': '' },
        { 'name': 'Sissy com Elevação Alta', 'url': 'https://www.inspireusafoundation.org/wp-content/uploads/2022/11/sissy-squat-muscles-768x569.png', 'category': 'Legs', 'nivel': 3, 'type': 'Parte da frente', 'division': 'Shrimp Squat (Push) - Parte da frente', 'required': '' },
        { 'name': 'Sissy com Elevação Média', 'url': 'https://www.inspireusafoundation.org/wp-content/uploads/2022/11/sissy-squat-muscles-768x569.png', 'category': 'Legs', 'nivel': 4, 'type': 'Parte da frente', 'division': 'Shrimp Squat (Push) - Parte da frente', 'required': '' },
        { 'name': 'Sissy com Elevação Minima', 'url': 'https://www.inspireusafoundation.org/wp-content/uploads/2022/11/sissy-squat-muscles-768x569.png', 'category': 'Legs', 'nivel': 5, 'type': 'Parte da frente', 'division': 'Shrimp Squat (Push) - Parte da frente', 'required': '' },
        { 'name': 'Sissy Squat', 'url': 'https://www.inspireusafoundation.org/wp-content/uploads/2022/11/sissy-squat-muscles-768x569.png', 'category': 'Legs', 'nivel': 6, 'type': 'Parte da frente', 'division': 'Shrimp Squat (Push) - Parte da frente', 'required': '' },
        { 'name': 'Tuck L-sit', 'url': 'https://calisthenicsfamily.b-cdn.net/wp-content/uploads/2021/04/Tuck-Planche-progression-Tucked-L-sit.png', 'category': 'Core', 'nivel': 1, 'type': 'Abdômen', 'division': 'L-sit (core) - Abdômen', 'required': 'paralelas', "segs": 'true' },
        { 'name': 'One Leg L-sit', 'url': 'https://bodydojo.com/wp-content/uploads/2018/09/single-leg-L-sit-parallettes-400x300.jpg', 'category': 'Core', 'nivel': 2, 'type': 'Abdômen', 'division': 'L-sit (core) - Abdômen', 'required': 'paralelas', "segs": 'true' },
        { 'name': 'L-sit', 'url': 'https://www.shutterstock.com/image-vector/l-sit-hang-on-bar-600w-796165771.jpg', 'category': 'Core', 'nivel': 3, 'type': 'Abdômen', 'division': 'L-sit (core) - Abdômen', 'default': 'true', 'required': 'barraFixa', "segs": 'true' },
        { 'name': 'Straddle L-sit', 'url': 'https://mover.tips/pics/exercise/s/straddle-l-sit.png', 'category': 'Core', 'nivel': 4, 'type': 'Abdômen', 'division': 'L-sit (core) - Abdômen', 'required': 'paralelas', "segs": 'true' },
        { 'name': 'Rings L-sit', 'url': 'https://i.ytimg.com/vi/lwcHmXvw-T4/maxresdefault.jpg', 'category': 'Core', 'nivel': 5, 'type': 'Abdômen', 'division': 'L-sit (core) - Abdômen', 'required': 'argolas', "segs": 'true' },
        { 'name': 'L-sit Supinado', 'url': 'https://i.ytimg.com/vi/WHi1bvZLwlw/maxresdefault.jpg', 'category': 'Core', 'nivel': 6, 'type': 'Abdômen', 'division': 'L-sit (core) - Abdômen', 'required': 'barraFixa', "segs": 'true' },
        { 'name': '60s de Prancha Abdominal', 'url': 'https://corpoesbelto.com.br/wp-content/uploads/2018/03/Exerc%C3%ADcio-de-Prancha.jpg', 'category': 'Core', 'nivel': 1, 'type': 'Abdômen', 'division': 'Abdominal na Rodinha - Abdômen', 'required': '', "segs": 'true' },
        { 'name': 'Prancha Abdominal Unilateral', 'url': 'https://treinomestre.com.br/wp-content/uploads/2021/07/prancha-lateral.jpg', 'category': 'Core', 'nivel': 2, 'type': 'Abdômen', 'division': 'Abdominal na Rodinha - Abdômen', 'required': '', "segs": 'true' },
        { 'name': 'Rodinha de Joelhos', 'url': 'https://treinomestre.com.br/wp-content/uploads/2017/02/roda-abdominal-exercicio.jpg', 'category': 'Core', 'nivel': 3, 'type': 'Abdômen', 'division': 'Abdominal na Rodinha - Abdômen', 'required': ['rodinha', 'argola'] },
        { 'name': 'Rodinha na Rampa Inclinada', 'url': 'https://treinomestre.com.br/wp-content/uploads/2017/02/roda-abdominal-exercicio.jpg', 'category': 'Core', 'nivel': 4, 'type': 'Abdômen', 'division': 'Abdominal na Rodinha - Abdômen', 'required': ['rodinha', 'argola'] },
        { 'name': 'Rodinha no chão Negativa', 'url': 'https://treinomestre.com.br/wp-content/uploads/2017/02/roda-abdominal-exercicio.jpg', 'category': 'Core', 'nivel': 5, 'type': 'Abdômen', 'division': 'Abdominal na Rodinha - Abdômen', 'required': ['rodinha', 'argola'] },
        { 'name': 'Rodinha no chão', 'url': 'https://treinomestre.com.br/wp-content/uploads/2017/02/roda-abdominal-exercicio.jpg', 'category': 'Core', 'nivel': 6, 'type': 'Abdômen', 'division': 'Abdominal na Rodinha - Abdômen', 'required': ['rodinha', 'argola'] },
        { 'name': 'Elevação de Perna Encolhida no Solo', 'url': 'https://i.ytimg.com/vi/SoX3_liHpZE/maxresdefault.jpg', 'category': 'Core', 'nivel': 1, 'type': 'Abdômen', 'division': 'Toes To Bar - Abdômen', 'required': '' },
        { 'name': 'Elevação de Perna no Solo', 'url': 'https://www.mundoboaforma.com.br/wp-content/uploads/2016/10/elevacao-de-pernas-e1475519816360.jpg', 'category': 'Core', 'nivel': 2, 'type': 'Abdômen', 'division': 'Toes To Bar - Abdômen', 'required': '' },
        { 'name': 'Meio Toes to Bar (perna até a metade)', 'url': 'https://i.ytimg.com/vi/6dHvTlsMvNY/maxresdefault.jpg', 'category': 'Core', 'nivel': 3, 'type': 'Abdômen', 'division': 'Toes To Bar - Abdômen', 'required': 'barraFixa' },
        { 'name': 'Straight Leg Toes to bar (até a barra)', 'url': 'https://i.ytimg.com/vi/6dHvTlsMvNY/maxresdefault.jpg', 'category': 'Core', 'nivel': 4, 'type': 'Abdômen', 'division': 'Toes To Bar - Abdômen', 'required': 'barraFixa' },
        { 'name': 'Straight Leg Toes to bar (até a barra)', 'url': 'https://i.ytimg.com/vi/6dHvTlsMvNY/maxresdefault.jpg', 'category': 'Core', 'nivel': 5, 'type': 'Abdômen', 'division': 'Toes To Bar - Abdômen', 'required': 'barraFixa' },
        { 'name': 'Weighted Toes to bar ', 'url': 'https://i.ytimg.com/vi/xX9Hzi7Onnw/maxresdefault.jpg', 'category': 'Core', 'nivel': 6, 'type': 'Abdômen', 'division': 'Toes To Bar - Abdômen', 'required': 'barraFixa' },
        { 'name': 'HR com Pernas Encolhida', 'url': 'https://cdn-0.weighttraining.guide/wp-content/uploads/2022/01/Flat-bench-reverse-hyperextension-1.png?ezimgfmt=ng%3Awebp%2Fngcb4', 'category': 'Core', 'nivel': 2, 'type': 'Lombar', 'division': 'Hiperextensão Reversa (HR) - Lombar', 'required': '' },
        { 'name': 'HR com 1 Perna', 'url': 'https://cdn-0.weighttraining.guide/wp-content/uploads/2022/01/Flat-bench-reverse-hyperextension-1.png?ezimgfmt=ng%3Awebp%2Fngcb4', 'category': 'Core', 'nivel': 3, 'type': 'Lombar', 'division': 'Hiperextensão Reversa (HR) - Lombar', 'required': '' },
        { 'name': 'Hiperextensão Reversa (Full)', 'url': 'https://i.4playercamp.cz/img/e8f1f106582bff976ac2dc1cc8009f.jpg', 'category': 'Core', 'nivel': 4, 'type': 'Lombar', 'division': 'Hiperextensão Reversa (HR) - Lombar', 'required': '' },{ 'name': 'Hiperextensão Reversa com Peso', 'url': 'https://sc02.alicdn.com/kf/HTB1zoEQRVXXXXX8XVXXq6xXFXXXi/222228634/HTB1zoEQRVXXXXX8XVXXq6xXFXXXi.jpg_.webp', 'category': 'Core', 'nivel': 6, 'type': 'Lombar', 'division': 'Hiperextensão Reversa (HR) - Lombar', 'required': '' },
        { 'name': 'Abdominal Remador', 'url': 'https://grandeatleta.com.br/wp-content/uploads/2021/02/abdominal-remador.jpg', 'nivel': 1, 'category': 'Core', 'type': 'Lombar', 'default': 'true', 'required': ''} ] 
        return exercises     

    def get_Name(name):
        filtered_data = list(filter(lambda e: e.get('name') == name , Exercicio.getAllExercicios()))
        if filtered_data:
            return filtered_data[0]
        else:
            return None
        
    def getAllCategory(category,array):
        filtered_data = list(filter(lambda e: e.get('category') == category , array)) 
        if filtered_data:
            return filtered_data
        else:
            return None    

    def getAllNivel(nivel,array):
        filtered_data = list(filter(lambda e: e.get('nivel') == nivel , array)) 
        if filtered_data:
            return filtered_data
        else:
            return None  

    def getSuggestionExerLight(name): 
    # nivel -1
        exer = Exercicio.get_Name(name)
        
        arrayCategory = Exercicio.getAllCategory(exer['category'], Exercicio.getAllExercicios())
        
        if isinstance(exer['nivel'], int):
            # Se for um número inteiro, use o valor diretamente
            filter = Exercicio.getAllNivel((exer['nivel'] + 1), arrayCategory)
            print(filter)
            return filter
        elif isinstance(exer['nivel'], list):
            # Se for uma lista, pegue o menor valor
            min_value = min(exer['nivel'])
            filter = Exercicio.getAllNivel((min_value + 1), arrayCategory)
            print(filter)
            return filter

   