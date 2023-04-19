const exercises = [
  { name: "Knee Push Ups (de joelho)", url: "https://cdn.w600.comps.canstockphoto.com.br/trabalhando-dela-joelho-femininas-vetor-clip-arte_csp89802369.jpg", category: "Push", nivel: 0, type: "Horizontal", division: "Flexão (Push Ups) - Horizontal", required: "" },
  { name: "Flexão Padrão", url: "https://aprovataf.com.br/wp-content/uploads/2016/04/Flex%C3%A3o-de-bra%C3%A7o-no-solo-AprovaTAF.jpg", category: "Push", nivel: 1, type: "Horizontal", division: "Flexão (Push Ups) - Horizontal", default: true, required: "" },
  { name: "Diamond Push Ups", url: "https://weighttraining.guide/wp-content/uploads/2017/07/diamond-push-up-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4", category: "Push", nivel: 2, type: "Horizontal", division: "Flexão (Push Ups) - Horizontal", required: "" },
  { name: "Archer Push Ups ", url: "https://images.squarespace-cdn.com/content/v1/5db20c73f80047725e83b73c/1605191028463-69TG5D2LHACZDGBUSVOX/service_1589888550_3778.jpg", category: "Push", nivel: 3, type: "Horizontal", division: "Flexão (Push Ups) - Horizontal", required: "" },
  { name: "Rings Push Ups", url: "https://www.fitstream.com/images/ring-training/exercises/ring-push-up.png?w=80&h=80", category: "Push", nivel: 4, type: "Horizontal", division: "Flexão (Push Ups) - Horizontal", required: "argolas" },
  { name: "One Arm Push Ups Elevada", url: "https://static.strengthlevel.com/images/illustrations/one-arm-push-ups-1000x1000.jpg", category: "Push", nivel: 5, type: "Horizontal", division: "Flexão (Push Ups) - Horizontal", required: "" },
  { name: "One Arm Push Ups/Tuck Planche", url: "https://post.healthline.com/wp-content/uploads/2019/07/Man-Exercising-1200x628-facebook.jpg", category: "Push", nivel: 6, type: "Horizontal", division: "Flexão (Push Ups) - Horizontal", required: "" },
  { name: "Bench Dips (Dips no banco)", url: "https://media.istockphoto.com/id/1277965681/pt/vetorial/bench-triceps-dips-female-exercise-guide-colorful-illustration.jpg?s=170667a&w=0&k=20&c=rys1gAWR29rv2zQL21jzAxKAmUhOaobuUjYkKQkOqj8=", category: "Push", nivel: 0, type: "Vertical", division: 'Dips - Vertical', required: "" },
  { name: "Dips com ajuda ou elastico", url: "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Dips.png/330px-Dips.png", category: "Push", nivel: 1, type: "Vertical", division: 'Dips - Vertical', required: ['paralelas', 'superband'] },
  { name: "Dips negativo", url: "https://julienquaglierini.com/wp-content/uploads/2018/08/dips-768x432.jpg.webp", category: "Push", nivel: 1, type: "Vertical", division: 'Dips - Vertical', required: "paralelas" },
  { name: "Dips na paralela", url: "https://static.netshoes.com.br/produtos/barra-paralela-dip-de-parede-calistenia-(parafusos-e-buchas-plasticas)/06/06O-0003-006/06O-0003-006_zoom3.jpg?ts=1601643646", category: "Push", nivel: 2, type: "Vertical", division: 'Dips - Vertical', default: true, required: "paralelas" },
  { name: "Dips na paralela", url: "https://static.netshoes.com.br/produtos/barra-paralela-dip-de-parede-calistenia-(parafusos-e-buchas-plasticas)/06/06O-0003-006/06O-0003-006_zoom3.jpg?ts=1601643646", category: "Push", nivel: 3, type: "Vertical", division: 'Dips - Vertical', default: true, required: "paralelas" },
  { name: "Dips em L-sit", url: "https://www.shutterstock.com/image-vector/male-athlete-silhouette-doing-calisthenics-600w-1348704965.jpg", category: "Push", nivel: 4, type: "Vertical", division: 'Dips - Vertical', required: ['paralelas', 'argolas'] },
  { name: "Dips a 45º (inclinado para frente)", url: "../img/Dips45ºpng.png", category: "Push", nivel: 4, type: "Vertical", division: 'Dips - Vertical', required: "paralelas" },
  { name: "Tuck Planche Push Ups", url: "https://qph.cf2.quoracdn.net/main-qimg-1782c86f06ca832b93dc8ae85ed637ae", category: "Push", nivel: 6, type: "Vertical", division: 'Dips - Vertical', required: "" },
  { name: "Rings Suppor Hold ", url: "https://bodydojo.com/wp-content/uploads/2018/06/RTO-support-400x300.jpg", category: "Push", nivel: 1, type: "Vertical", division: "Dips na Argola - Vertical", required: "argolas" },
  { name: "Rings Suppor Hold Supinado", url: "https://s3.amazonaws.com/prod.skimble/assets/832102/image_iphone.jpg", category: "Push", nivel: 2, type: "Vertical", division: "Dips na Argola - Vertical", required: "argolas" },
  { name: "Ring Dips Negativo", url: "https://img.myloview.com.br/fotomurais/woman-doing-gymnastic-ring-dips-exercise-flat-vector-illustration-isolated-on-white-background-700-277885449.jpg", category: "Push", nivel: 3, type: "Vertical", division: "Dips na Argola - Vertical", required: "argolas" },
  { name: "Ring Dips", url: "https://previews.123rf.com/images/lioputra/lioputra2011/lioputra201100076/158973747-gymnastic-ring-dips-exercise-flat-vector-illustration-isolated-on-white-background-workout.jpg", category: "Push", nivel: 4, type: "Vertical", division: "Dips na Argola - Vertical", required: "argolas" },
  { name: "Dips em L-sit/Buldarian Dips", url: "https://cdn.vectorstock.com/i/1000x1000/05/62/man-doing-chair-bench-tricep-dips-exercise-vector-42870562.webp", category: "Push", nivel: 5, type: "Vertical", division: "Dips na Argola - Vertical", required: "" },
  { name: "Ring Dips Supinado", url: "https://www.shutterstock.com/image-vector/sporty-man-doing-ring-dips-600w-1360756589.jpg", category: "Push", nivel: 6, type: "Vertical", division: "Dips na Argola - Vertical", required: "argolas" },
  { name: "Dips com ajuda", url: "https://thumbs.dreamstime.com/z/ilustra%C3%A7%C3%A3o-de-vetor-for%C3%A7a-exerc%C3%ADcio-barra-dip-do-varejo-com-fundo-branco-vetorial-215590449.jpg", category: "Push", nivel: 1, type: "Vertical", division: "Weigthed Dips - Vertical", required: " paralelas" },
  { name: "Dips na paralela", url: "https://static.netshoes.com.br/produtos/barra-paralela-dip-de-parede-calistenia-(parafusos-e-buchas-plasticas)/06/06O-0003-006/06O-0003-006_zoom3.jpg?ts=1601643646", category: "Push", nivel: 3, type: "Vertical", division: "Weigthed Dips - Vertical", required: "paralelas" },
  { name: "Dips + 20% do seu peso", url: "https://ginasiovirtual.com/wp-content/uploads/2021/06/fundos-com-peso.jpg", category: "Push", nivel: 4, type: "Vertical", division: "Weigthed Dips - Vertical", required: "paralelas" },
  { name: "Dips + 38% do seu peso", url: "https://ginasiovirtual.com/wp-content/uploads/2021/06/fundos-com-peso.jpg", category: "Push", nivel: 5, type: "Vertical", division: "Weigthed Dips - Vertical", required: "paralelas" },
  { name: "Dips + 55% do seu peso ", url: "https://ginasiovirtual.com/wp-content/uploads/2021/06/fundos-com-peso.jpg", category: "Push", nivel: 6, type: "Vertical", division: "Weigthed Dips - Vertical", required: "paralelas" },
  { name: "Pike Push Ups", url: "https://qph.cf2.quoracdn.net/main-qimg-47c44c047bbb8118ed02ff236da07841-lq", category: "Push", nivel: 1, type: "Vertical", division: "Flexão na Parada de Mãos - Vertical", required: "" },
  { name: "Elevated Pike PU", url: "https://b1494239.smushcdn.com/1494239/wp-content/uploads/2013/12/pike-push-up-advanced-e1438882945766.jpg?lossy=0&strip=1&webp=1", category: "Push", nivel: 2, type: "Vertical", division: "Flexão na Parada de Mãos - Vertical", required: "" },
  { name: "HSPU Negativo com kick | sem kick", url: "https://www.getpersonalgrowth.com/images/posts/8a57dd56ac409541f34d096ff1f903f4-0.jpg", category: "Push", nivel: 3, type: "Vertical", division: "Flexão na Parada de Mãos - Vertical", required: "" },
  { name: "Wall HSPU (Handstand Push Ups)", url: "https://images.contentstack.io/v3/assets/blt45c082eaf9747747/blt2c3e741ea4156df4/5dee7c59d03adf37d49cc286/Florian_HSPU_ES_HEAD.jpg?format=pjpg&auto=webp&quality=76&width=716", category: "Push", nivel: 4, type: "Vertical", division: "Flexão na Parada de Mãos - Vertical", required: "" },
  { name: "Wall HSPU c/ Paralela de frente | de costas", url: "https://elemento.ag/blog/wp-content/uploads/2022/02/image6.jpg", category: "Push", nivel: 5, type: "Vertical", division: "Flexão na Parada de Mãos - Vertical", required: "" },
  { name: "HSPU Livre", url: "https://http2.mlstatic.com/D_NQ_NP_2X_813656-MLB46427391074_062021-F.webp", category: "Push", nivel: 6, type: "Vertical", division: "Flexão na Parada de Mãos - Vertical", required: "" },

  { name: "Negativas de Remada", url: "https://treinomestre.com.br/wp-content/uploads/2021/11/remada-articulada.jpg", category: "Pull", nivel: 1, type: "Horizontal", division: " Rows/Barra Australiana - Horizontal", required: ['argolas', 'paralelas', 'barraFixa', 'trx'] },
  { name: "Rows/Barra Australiana", url: "https://www.sport.es/labolsadelcorredor/wp-content/uploads/2018/05/Australian-pull-up.jpg", category: "Pull", nivel: 2, type: "Horizontal", division: " Rows/Barra Australiana - Horizontal", default: true, required: ['argolas', 'paralelas', 'barraFixa', 'trx'] },
  { name: "Wide Rows (pegada aberta)", url: "https://www.spotebi.com/wp-content/uploads/2015/04/wide-row-exercise-illustration.jpg", category: "Pull", nivel: 3, type: "Horizontal", division: " Rows/Barra Australiana - Horizontal", required: ['argolas', 'paralelas', 'barraFixa', 'trx'] },
  { name: "Archer Rows Braços Dobrados ou Alta", url: "https://cdn.vectorstock.com/i/1000x1000/36/80/woman-doing-upper-back-exercise-archer-with-long-r-vector-43113680.webp", category: "Pull", nivel: 4, type: "Horizontal", division: " Rows/Barra Australiana - Horizontal", required: "" },
  { name: "Archer Rows (braço esticado)/Tuck Front Lever", url: "https://cdn.vectorstock.com/i/1000x1000/36/80/woman-doing-upper-back-exercise-archer-with-long-r-vector-43113680.webp", category: "Pull", nivel: 5, type: "Horizontal", division: " Rows/Barra Australiana - Horizontal", required: ['argolas', 'paralelas', 'barraFixa', 'trx'] },
  { name: "Straddle One Arm Rows", url: "https://www.shutterstock.com/image-vector/man-doing-single-arm-bent-600w-2101536073.jpg", category: "Pull", nivel: 6, type: "Horizontal", division: " Rows/Barra Australiana - Horizontal", required: ['argolas', 'paralelas', 'barraFixa', 'trx'] },
  { name: "Pull Ups com ajuda ou elastico", url: "https://network.grupoabril.com.br/wp-content/uploads/sites/2/2017/01/xxxx.jpg?quality=85&strip=all&w=1024", category: "Pull", nivel: 0, type: "Vertical", division: "Barra Fixa (Pull Ups) - Vertical", required: ['barraFixa', 'superband'] },
  { name: "Pull Ups negativo", url: "https://www.fitstream.com/images/bodyweight-training/bodyweight-exercises/negative-pull-up-main.png", category: "Pull", nivel: 2, type: "Vertical", division: "Barra Fixa (Pull Ups) - Vertical", required: "barraFixa" },
  { name: "Pull Ups", url: "http://2.bp.blogspot.com/-kKolopOtBl8/UDvUdp8cDTI/AAAAAAAABw8/KwV1AzFxPsE/s400/FITNESS_proradicalskate.jpg", category: "Pull", nivel: 3, type: "Vertical", division: "Barra Fixa (Pull Ups) - Vertical", default: true, required: "barraFixa" },
  { name: "Pull Ups em L-sit", url: "https://i.pinimg.com/564x/f3/b2/eb/f3b2eb20fc9472333072dab45e4140a6.jpg", category: "Pull", nivel: 4, type: "Vertical", division: "Barra Fixa (Pull Ups) - Vertical", required: "barraFixa" },
  { name: "Wide Pull Ups (pegada aberta)", url: "https://images.squarespace-cdn.com/content/v1/57efdb4cd482e918dc2a900f/1658358689971-JZXGL3SS7MY5ES2S9VVT/extra+wide+pull+up+grip.JPG?format=500w", category: "Pull", nivel: 5, type: "Vertical", division: "Barra Fixa (Pull Ups) - Vertical", required: "barraFixa" },
  { name: "Wide Pull Ups em L-sit", url: "https://www.fitliferegime.com/wp-content/uploads/2023/01/Muscle-Worked-During-Pull-Ups-1024x683.webp?ezimgfmt=ng:webp/ngcb1", category: "Pull", nivel: 6, type: "Vertical", division: "Barra Fixa (Pull Ups) - Vertical", required: "barraFixa" },
  { name: "Archer Pull ups", url: "https://kengurupro.eu/wp-content/uploads/2020/10/k-005-1-1.jpg", category: "Pull", nivel: 6, type: "Vertical", division: "One Arm Pull Ups (um braço) - Vertical", required: "barraFixa" },
  { name: "Pull Ups com ajuda", url: "https://network.grupoabril.com.br/wp-content/uploads/sites/2/2017/01/xxxx.jpg?quality=85&strip=all&w=1024", category: "Pull", nivel: 1, type: "Vertical", division: "Weigthed Pull Ups - Vertical", required: "barraFixa" },
  // { name: "Pull Ups negativo", url: "https://www.fitstream.com/images/bodyweight-training/bodyweight-exercises/negative-pull-up-main.png", category: "Pull", nivel: 2, type: "Vertical", division: "Weigthed Pull Ups - Vertical", required:"" },
  { name: "Pull Ups", url: "http://2.bp.blogspot.com/-kKolopOtBl8/UDvUdp8cDTI/AAAAAAAABw8/KwV1AzFxPsE/s400/FITNESS_proradicalskate.jpg", category: "Pull", nivel: 3, type: "Vertical", division: "Weigthed Pull Ups - Vertical", required: "barraFixa" },
  { name: "Pull Ups +18% seu peso", url: "https://st4.depositphotos.com/13768208/40092/i/450/depositphotos_400928346-stock-photo-cross-fit-seminar-staff-member.jpg", category: "Pull", nivel: 4, type: "Vertical", division: "Weigthed Pull Ups - Vertical", required: "barraFixa" },
  { name: "Pull Ups +35% seu peso", url: "https://st4.depositphotos.com/13768208/40092/i/450/depositphotos_400928346-stock-photo-cross-fit-seminar-staff-member.jpg", category: "Pull", nivel: 5, type: "Vertical", division: "Weigthed Pull Ups - Vertical", required: "barraFixa" },
  { name: "Pull Ups +50% seu peso", url: "https://st4.depositphotos.com/13768208/40092/i/450/depositphotos_400928346-stock-photo-cross-fit-seminar-staff-member.jpg", category: "Pull", nivel: 6, type: "Vertical", division: "Weigthed Pull Ups - Vertical", required: "barraFixa" },
  { name: "Kipping Pull-ups", url: "https://i.ytimg.com/vi_webp/AyPTCEXTjOo/maxresdefault.webp", category: "Pull", nivel: 2, type: "Vertical", division: "Pull Ups Explosivos - Vertical", required: "barraFixa" },
  { name: "Pull-ups", url: "http://2.bp.blogspot.com/-kKolopOtBl8/UDvUdp8cDTI/AAAAAAAABw8/KwV1AzFxPsE/s400/FITNESS_proradicalskate.jpg", category: "Pull", nivel: 3, type: "Vertical", division: "Pull Ups Explosivos - Vertical", required: "barraFixa" },
  { name: "Kipping Pull-ups com Palma", url: "https://i.ytimg.com/vi_webp/AyPTCEXTjOo/maxresdefault.webp", category: "Pull", nivel: 4, type: "Vertical", division: "Pull Ups Explosivos - Vertical", required: "barraFixa" },
  { name: "Pull-ups com Palma sem Kipping", url: "https://doutorjairo.uol.com.br/media/uploads/istock-923748448.jpg", category: "Pull", nivel: 5, type: "Vertical", division: "Pull Ups Explosivos - Vertical", required: "barraFixa" },
  { name: "L-sit Pull-ups com Palma", url: "https://i.pinimg.com/564x/f3/b2/eb/f3b2eb20fc9472333072dab45e4140a6.jpg", category: "Pull", nivel: 6, type: "Vertical", division: "Pull Ups Explosivos - Vertical", required: "barraFixa" },
  { name: "Squat 45º", url: "https://static.tuasaude.com/media/article/3k/ru/6-exercicios-de-agachamento-para-gluteos_9131_l.jpg", category: "Legs", nivel: 1, type: "Parte da frente", division: "Squat (Push) - Parte da frente", required: "" },
  { name: "Full Squat (descer tudo)", url: "https://static.vecteezy.com/ti/vetor-gratis/p2/8635575-mulher-fazendo-peso-corporal-agachamento-exercicio-plano-ilustracao-isolado-em-fundo-branco-vetor.jpg", category: "Legs", nivel: 2, type: "Parte da frente", division: "Squat (Push) - Parte da frente", default: true, required: "" },
  { name: "Side to Side Squat", url: "https://www.spotebi.com/wp-content/uploads/2015/02/side-to-side-squats-exercise-illustration.jpg", category: "Legs", nivel: 3, type: "Parte da frente", division: "Squat (Push) - Parte da frente", required: "" },
  { name: "Pistol", url: "https://www.spotebi.com/wp-content/uploads/2015/05/pistol-squat-exercise-illustration.jpg", category: "Legs", nivel: 4, type: "Parte da frente", division: "Squat (Push) - Parte da frente", required: "" },
  { name: "Pistol + 20% seu peso", url: "https://horadotreino.com.br/wp-content/uploads/2013/12/agachamento-unilateral2.jpg", category: "Legs", nivel: 5, type: "Parte da frente", division: "Squat (Push) - Parte da frente", required: "" },
  { name: "Pistol + 35% seu peso", url: "https://horadotreino.com.br/wp-content/uploads/2013/12/agachamento-unilateral2.jpg", category: "Legs", nivel: 6, type: "Parte da frente", division: "Squat (Push) - Parte da frente", required: "" },
  { name: "Hip Thruster", url: "https://thumbs.dreamstime.com/z/mulher-fazendo-levantamentos-eleva%C3%A7%C3%A3o-da-bunda-exerc%C3%ADcio-de-pontes-que-exercem-uma-ilustra%C3%A7%C3%A3o-plana-do-vetor-isolada-em-fundo-236723402.jpg", category: "Legs", nivel: 1, type: "Parte de trás", division: "Hip Thruster (Pull) - Parte de trás", default: true, required: "" },
  { name: "Elevated Hip Thruster", url: "https://doctorlib.info/sport/mens-health-body/mens-health-body.files/image024.jpg", category: "Legs", nivel: 2, type: "Parte de trás", division: "Hip Thruster (Pull) - Parte de trás", required: "" },
  { name: "One Leg Hip Thruster", url: "https://cdn-0.weighttraining.guide/wp-content/uploads/2017/08/weighted-one-leg-hip-thrust-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4", category: "Legs", nivel: 3, type: "Parte de trás", division: "Hip Thruster (Pull) - Parte de trás", required: "" },
  { name: "Weighted Hip Thruster", url: "https://cdn-0.weighttraining.guide/wp-content/uploads/2017/04/barbell-hip-thrust-resized.png?ezimgfmt=ng%3Awebp%2Fngcb4", category: "Legs", nivel: 4, type: "Parte de trás", division: "Hip Thruster (Pull) - Parte de trás", required: "" },
  { name: "Stiff Unilateral", url: "https://i.pinimg.com/564x/9d/6d/a9/9d6da9c12158ec52d1f660bf12fa490c.jpg", category: "Legs", nivel: 1, type: "Parte de trás", division: "Nordic Curls (Pull) - Parte de trás", required: "" },
  { name: "Flexão de Tronco", url: "https://thumbs.dreamstime.com/z/exerc%C3%ADcio-da-aptid%C3%A3o-flex%C3%A3o-do-tronco-com-eleva%C3%A7%C3%A3o-da-pelve-que-encontra-se-no-assoalho-f%C3%AAmea-64591838.jpg", category: "Legs", nivel: 2, type: "Parte de trás", division: "Nordic Curls (Pull) - Parte de trás", required: "" },
  { name: "Nordic Cruls 45º", url: "https://en.pimg.jp/076/410/785/1/76410785.jpg", category: "Legs", nivel: 3, type: "Parte de trás", division: "Nordic Curls (Pull) - Parte de trás", required: "" },
  { name: "Nordic Cruls Negativo", url: "https://en.pimg.jp/076/410/785/1/76410785.jpg", category: "Legs", nivel: 4, type: "Parte de trás", division: "Nordic Curls (Pull) - Parte de trás", required: "" },
  { name: "Nordic Curls", url: "https://hips.hearstapps.com/hmg-prod/images/screen-shot-2021-10-12-at-11-31-36-am-1634052723.png", category: "Legs", nivel: 5, type: "Parte de trás", division: "Nordic Curls (Pull) - Parte de trás", required: "" },
  { name: "Nordic Curls/braços para cima", url: "https://hips.hearstapps.com/hmg-prod/images/screen-shot-2021-10-12-at-11-31-36-am-1634052723.png", category: "Legs", nivel: 6, type: "Parte de trás", division: "Nordic Curls (Pull) - Parte de trás", required: "" },
  { name: "Afundo/Bulgarian Squat", url: "https://cdn-0.weighttraining.guide/wp-content/uploads/2021/10/Bulgarian-split-squat.png?ezimgfmt=ng%3Awebp%2Fngcb4", category: "Legs", nivel: 2, type: "Parte da frente", division: "Shrimp Squat (Push) - Parte da frente", required: "" },
  { name: "Shrimp com apoio no joelho", url: "https://www.getstrong.fit/images/Shrimp-Squat.jpg?ezimgfmt=rs:620x347/rscb1/ng:webp/ngcb1", category: "Legs", nivel: 3, type: "Parte da frente", division: "Shrimp Squat (Push) - Parte da frente", required: "" },
  { name: "Shrimp com joelho ao chão", url: "https://www.getstrong.fit/images/Shrimp-Squat.jpg?ezimgfmt=rs:620x347/rscb1/ng:webp/ngcb1", category: "Legs", nivel: 4, type: "Parte da frente", division: "Shrimp Squat (Push) - Parte da frente", required: "" },
  { name: "One Hand Shrimp", url: "https://www.getstrong.fit/images/Shrimp-Squat.jpg?ezimgfmt=rs:620x347/rscb1/ng:webp/ngcb1", category: "Legs", nivel: 5, type: "Parte da frente", division: "Shrimp Squat (Push) - Parte da frente", required: "" },
  { name: "2 Hands Shrimp", url: "https://www.getstrong.fit/images/Shrimp-Squat.jpg?ezimgfmt=rs:620x347/rscb1/ng:webp/ngcb1", category: "Legs", nivel: 6, type: "Parte da frente", division: "Shrimp Squat (Push) - Parte da frente", required: "" },
  { name: "Reverse Nordic Curls | Smith Sissy", url: "https://fitnessvolt.com/wp-content/uploads/2022/10/Reverse-Nordic-Curl-Guide-750x422.jpg", category: "Legs", nivel: 2, type: "Parte da frente", division: "Shrimp Squat (Push) - Parte da frente", required: "" },
  { name: "Sissy com Elevação Alta", url: "https://www.inspireusafoundation.org/wp-content/uploads/2022/11/sissy-squat-muscles-768x569.png", category: "Legs", nivel: 3, type: "Parte da frente", division: "Shrimp Squat (Push) - Parte da frente", required: "" },
  { name: "Sissy com Elevação Média", url: "https://www.inspireusafoundation.org/wp-content/uploads/2022/11/sissy-squat-muscles-768x569.png", category: "Legs", nivel: 4, type: "Parte da frente", division: "Shrimp Squat (Push) - Parte da frente", required: "" },
  { name: "Sissy com Elevação Minima", url: "https://www.inspireusafoundation.org/wp-content/uploads/2022/11/sissy-squat-muscles-768x569.png", category: "Legs", nivel: 5, type: "Parte da frente", division: "Shrimp Squat (Push) - Parte da frente", required: "" },
  { name: "Sissy Squat", url: "https://www.inspireusafoundation.org/wp-content/uploads/2022/11/sissy-squat-muscles-768x569.png", category: "Legs", nivel: 6, type: "Parte da frente", division: "Shrimp Squat (Push) - Parte da frente", required: "" },
  { name: "Tuck L-sit", url: "https://calisthenicsfamily.b-cdn.net/wp-content/uploads/2021/04/Tuck-Planche-progression-Tucked-L-sit.png", category: "Core", nivel: 1, type: "Abdômen", division: "L-sit (core) - Abdômen", required: "paralelas", segs: true },
  { name: "One Leg L-sit", url: "https://bodydojo.com/wp-content/uploads/2018/09/single-leg-L-sit-parallettes-400x300.jpg", category: "Core", nivel: 2, type: "Abdômen", division: "L-sit (core) - Abdômen", required: "paralelas", segs: true },
  { name: "L-sit", url: "https://www.shutterstock.com/image-vector/l-sit-hang-on-bar-600w-796165771.jpg", category: "Core", nivel: 3, type: "Abdômen", division: "L-sit (core) - Abdômen", default: true, required: "barraFixa", segs: true },
  { name: "Straddle L-sit", url: "https://mover.tips/pics/exercise/s/straddle-l-sit.png", category: "Core", nivel: 4, type: "Abdômen", division: "L-sit (core) - Abdômen", required: "paralelas", segs: true },
  { name: "Rings L-sit", url: "https://i.ytimg.com/vi/lwcHmXvw-T4/maxresdefault.jpg", category: "Core", nivel: 5, type: "Abdômen", division: "L-sit (core) - Abdômen", required: "argolas", segs: true },
  { name: "L-sit Supinado", url: "https://i.ytimg.com/vi/WHi1bvZLwlw/maxresdefault.jpg", category: "Core", nivel: 6, type: "Abdômen", division: "L-sit (core) - Abdômen", required: "barraFixa", segs: true },
  { name: "60s de Prancha Abdominal", url: "https://corpoesbelto.com.br/wp-content/uploads/2018/03/Exerc%C3%ADcio-de-Prancha.jpg", category: "Core", nivel: 1, type: "Abdômen", division: "Abdominal na Rodinha - Abdômen", required: "", segs: true },
  { name: "Prancha Abdominal Unilateral", url: "https://treinomestre.com.br/wp-content/uploads/2021/07/prancha-lateral.jpg", category: "Core", nivel: 2, type: "Abdômen", division: "Abdominal na Rodinha - Abdômen", required: "", segs: true },
  { name: "Rodinha de Joelhos", url: "https://treinomestre.com.br/wp-content/uploads/2017/02/roda-abdominal-exercicio.jpg", category: "Core", nivel: 3, type: "Abdômen", division: "Abdominal na Rodinha - Abdômen", required: ['rodinha', 'argola'] },
  { name: "Rodinha na Rampa Inclinada", url: "https://treinomestre.com.br/wp-content/uploads/2017/02/roda-abdominal-exercicio.jpg", category: "Core", nivel: 4, type: "Abdômen", division: "Abdominal na Rodinha - Abdômen", required: ['rodinha', 'argola'] },
  { name: "Rodinha no chão Negativa", url: "https://treinomestre.com.br/wp-content/uploads/2017/02/roda-abdominal-exercicio.jpg", category: "Core", nivel: 5, type: "Abdômen", division: "Abdominal na Rodinha - Abdômen", required: ['rodinha', 'argola'] },
  { name: "Rodinha no chão", url: "https://treinomestre.com.br/wp-content/uploads/2017/02/roda-abdominal-exercicio.jpg", category: "Core", nivel: 6, type: "Abdômen", division: "Abdominal na Rodinha - Abdômen", required: ['rodinha', 'argola'] },
  { name: "Elevação de Perna Encolhida no Solo", url: "https://i.ytimg.com/vi/SoX3_liHpZE/maxresdefault.jpg", category: "Core", nivel: 1, type: "Abdômen", division: "Toes To Bar - Abdômen", required: "" },
  { name: "Elevação de Perna no Solo", url: "https://www.mundoboaforma.com.br/wp-content/uploads/2016/10/elevacao-de-pernas-e1475519816360.jpg", category: "Core", nivel: 2, type: "Abdômen", division: "Toes To Bar - Abdômen", required: "" },
  { name: "Meio Toes to Bar (perna até a metade)", url: "https://i.ytimg.com/vi/6dHvTlsMvNY/maxresdefault.jpg", category: "Core", nivel: 3, type: "Abdômen", division: "Toes To Bar - Abdômen", required: "barraFixa" },
  { name: "Straight Leg Toes to bar (até a barra)", url: "https://i.ytimg.com/vi/6dHvTlsMvNY/maxresdefault.jpg", category: "Core", nivel: 4, type: "Abdômen", division: "Toes To Bar - Abdômen", required: "barraFixa" },
  { name: "Straight Leg Toes to bar (até a barra)", url: "https://i.ytimg.com/vi/6dHvTlsMvNY/maxresdefault.jpg", category: "Core", nivel: 5, type: "Abdômen", division: "Toes To Bar - Abdômen", required: "barraFixa" },
  { name: "Weighted Toes to bar ", url: "https://i.ytimg.com/vi/xX9Hzi7Onnw/maxresdefault.jpg", category: "Core", nivel: 6, type: "Abdômen", division: "Toes To Bar - Abdômen", required: "barraFixa" },
  { name: "HR com Pernas Encolhida", url: "https://cdn-0.weighttraining.guide/wp-content/uploads/2022/01/Flat-bench-reverse-hyperextension-1.png?ezimgfmt=ng%3Awebp%2Fngcb4", category: "Core", nivel: 2, type: "Lombar", division: "Hiperextensão Reversa (HR) - Lombar", required: "" },
  { name: "HR com 1 Perna", url: "https://cdn-0.weighttraining.guide/wp-content/uploads/2022/01/Flat-bench-reverse-hyperextension-1.png?ezimgfmt=ng%3Awebp%2Fngcb4", category: "Core", nivel: 3, type: "Lombar", division: "Hiperextensão Reversa (HR) - Lombar", required: "" },
  { name: "Hiperextensão Reversa (Full)", url: "https://i.4playercamp.cz/img/e8f1f106582bff976ac2dc1cc8009f.jpg", category: "Core", nivel: 4, type: "Lombar", division: "Hiperextensão Reversa (HR) - Lombar", required: "" },
  { name: "Hiperextensão Reversa com Peso", url: "https://sc02.alicdn.com/kf/HTB1zoEQRVXXXXX8XVXXq6xXFXXXi/222228634/HTB1zoEQRVXXXXX8XVXXq6xXFXXXi.jpg_.webp", category: "Core", nivel: 6, type: "Lombar", division: "Hiperextensão Reversa (HR) - Lombar", required: "" },
  { name: "Abdominal Remador", url: "https://grandeatleta.com.br/wp-content/uploads/2021/02/abdominal-remador.jpg", nivel: 1, category: "Core", type: "Lombar", default: true, required: "" }

]

const exercisesBase = exercises.filter(e => e.default == true)

const div2 = document.getElementById('div2');



window.addEventListener("load", function () {
});

var treino = []
var newExercises = []
var newExercisesBase = []
var requireds = []
var numberInput = [1, 2, 3, 4, 5, 6, 7, 8]

function getImgUrl(name) {
  const exercise = exercises.find(e => e.name === name);
  return exercise.url;
}

function creatExercisesBase() {
  //Esconde
  const quiz = document.getElementById('quiz')
  quiz.classList.add('d-none')


  const btnGera = document.getElementById('btnGera')
  btnGera.classList.remove('d-none')
  // Div onde sera add os exercicios
  const divPai2 = document.getElementById('div2')
  var x = 1
  divPai2.classList.remove('d-none')



  newExercisesBase.forEach(exer => {

    if (exer == undefined) {
      return
    }
    // Criação da nova div
    var novaDiv = document.createElement("div");
    novaDiv.id = "exer" + x;
    novaDiv.className = "col-lg-5 position-relative col-11 d-flex justify-content-center align-items-center rounded-3 p-2 m-2 bg-white";
    novaDiv.style.border = "1px solid rgb(163, 163, 163)";

    // Criação do conteúdo da div
    novaDiv.innerHTML = `
      <div class="row position-relative">
        <div class="col-3 d-flex justify-content-center align-items-center">
          <img class="rounded-4" id="${'img' + x}" width="68" height="68"
            src="${exer.url}"
            alt="">
        </div>

        <div class="col-9 d-flex align-items-center ps-3 pe-5">
          <div class="row">
            <div class="col-12 reset-Padding">
              <input type="hidden" id=${'nivel' + x} name="nivel" value="${exer.nivel}">
              <span id=${'ValidTitle' + x} class="reset text-uppercase" style="font-size: 18px;">${exer.name}</span>
            </div>

            <div class="col-4 d-flex flex-column justify-content-center align-items-start my-2 reset-Padding">
              <p class="reset text-uppercase text-gray1">SÉRIE</p>
              <input class="w-75 text-center rounded-3" type="text" placeholder="1" disabled>
            </div>

            <div class="col-4 d-flex flex-column justify-content-center align-items-center reset-Padding">
              <p id="${'repts' + x}" class="reset text-uppercase text-gray1">${exer.segs ? 'SEGS' : 'REPS'}</p>
              <input pattern="^-?\d*\.?\d+$" inputmode="numeric" required="true" id="${'ValidExer' + x}" class="w-75 input-value text-center rounded-3" type="number">

            </div>

            <div class="col-4 d-flex flex-column justify-content-center align-items-end reset-Padding">
              <p class="reset text-uppercase text-gray1">PAUSA</p>
              <input required="true" disabled placeholder="3min"
                class="w-75 input-value text-center rounded-3" type="text">
            </div>
          </div>

           <!--<i class="bi bi-three-dots-vertical position-absolute top-0 end-0 "></i>-->
        </div>

        <div id="${'toggleExer' + x}"class="col-12 d-none d-flex flex-column justify-content-center">

          <button id="${'btn' + x}" onclick="filter(${x}, '${exer.name}', '${exer.category}', '${exer.type}', ${exer.nivel})" class="btn btn-primary mb-2 w-100" data-bs-toggle="modal" data-bs-target="#exampleModal">Trocar Exercicío</button>
            
          </button>

            <span id="${'heavy' + x}" class="reset text-danger text-start px-2 d-none" style="font-size: 10px;">
                    *Ops, sua quantidade de ${exer.segs ? 'segundos' : 'repetição'} está baixa! Vamos trocar para um mais leve?
                </span>

                 <span id="${'light' + x}" class="reset text-danger text-start px-2 d-none" style="font-size: 10px;">
                    *Ops, sua quantidade de ${exer.segs ? 'segundos' : 'repetição'} está  alta! Vamos trocar para um mais pesado?
                </span> 

                </div>
                <span id="${'success' + x}" class="reset px-3 text-start text-success d-none" style="font-size: 10px;">
                Perfeito, agora é só descansar <span id="cronometro"></span> e fazer o próximo exercício
                </span> 

                <span id="${'noInput' + x}" class="reset px-3 text-start text-danger d-none" style="font-size: 10px;">
                Por favor, insira o numero máximo de ${exer.segs ? 'segundos' : 'repetição'}, para montarmos seu treino.
                </span> 
      </div>`;
    x += 1
    divPai2.appendChild(novaDiv)
  })

  // Criando as verificações "Blur"
  for (let i = 1; i < newExercisesBase.length + 1; i++) {
    creatStruct(i)
  }

}

function filter(id, name, category, type, nivel) {

  // Mescla os dados entre os arrays
  let arrayCorrecty = correctingArray(treino, exercises)
  // Procura no array de exercicios qual é o que vai ser alterado
  let exerFound = exercises.filter(e => e.name == name)

  let filterType


  const divHidden = document.getElementById('divToggle')
  divHidden.classList.remove('d-none')
  divHidden.classList.add('d-block')

  const inputValue = document.getElementById('ValidExer' + id)
  let input = parseInt(inputValue.value)


  nivel = exerFound[0].nivel
  let segs = exerFound[0].segs
  // Verifica se o exercicio precisa tratar segundos
  if (segs) {
    //input 18s
    let segundos = input / 2 //9s
    let repeticao = 60 / segundos // 6 reptes
    let sugundosTotais = segundos * repeticao // 54segundos totais
    if (repeticao == 5 || repeticao == 6) {

    }
    if (repeticao > 6 || input <= 60) {
      nivel -= 1
    }
    if (repeticao < 2) {
      nivel += 1
    }

  }
  else {

    if (input != null) {
      input == 0 || input <= 2 ? nivel -= 2 : null;

      input >= 3 && input <= 5 ? nivel -= 1 : null;

      input >= 6 && input <= 15 ? nivel : null  // valor ser mostrado default

      input > 15 && input <= 25 ? nivel += 1 : null;

      input > 25 && input <= 40 ? nivel += 2 : null;

      nivel > 6 ? nivel = 6 : nivel = nivel

      nivel < 0 ? nivel = 0 : nivel = nivel
    }

  }


  if (category) {
    filterType = newExercises.filter(exercise => exercise.category === category);
  }
  // Filtra os exercícios com base no nível, se o nível for especificado
  if (nivel !== undefined && nivel >= 0) {
    filterType = filterType.filter(exercise => exercise.nivel === nivel);
  }
  // Filtra os exercícios com base no tipo, se o tipo for especificado
  if (type) {
    filterType = filterType.filter(exercise => exercise.type === type);
  }


  // Retira exercicios repetidos
  let filtered = filterType.filter((item, index, arr) => {
    return arr.findIndex(t => t.name === item.name) === index;
  });
  filterType = filtered;

  // Retira os exercicios que estão no newExercisesBase
  let altered = [];
  filterType.forEach(e => {
    if (!newExercisesBase.find(i => i.name === e.name)) {
      altered.push(e);
    }
  });
  filterType = altered;


  // Retira todos os exercicios com o nome do que está subistituindo
  filterType = filterType.filter(e => e.name !== exerFound[0].name);

  if (filterType.length < 1) {
    const zeroExer = document.getElementById('zeroExer')
    zeroExer.classList.add('d-none')
    const exerLeve = document.getElementById('exerLeve')
    exerLeve.classList.add('d-none')

    let exerSameCategory = arrayCorrecty.filter(e => e.category == exerFound[0].category && e.name != exerFound[0].name)


    // Se não tiver outro exercicio no treino 
    if (exerSameCategory.length > 0) {
      //Mostrar messagem que só tera esse exercicio até ele evoluir o suficiente para fazer outro exercicio
      const exerLeve = document.getElementById('exerLeve')
      exerLeve.classList.remove('d-none')

      const ESC = document.getElementById('exerSameCategory')
      ESC.innerHTML = exerSameCategory[0].name

      const titleModal = document.getElementById('exampleModalLabel')
      titleModal.innerHTML = 'Atenção'
      titleModal.classList.add('fw-bolder')

      const exerLeveRemove = document.getElementById('exerLeveRemove')
      exerLeveRemove.onclick = function () { removeExer(exerFound) };

    }
    else {
      // Identificamos qual é o outro exercicio da mesma categoria
      let otherExerSameCategory = newExercisesBase.filter(e => e.category == exerFound[0].category && e.name != exerFound[0].name)[0]
      // descobrimos o index dele
      let index = newExercisesBase.findIndex(e => e.name == otherExerSameCategory.name)
      // Atraves do index puxamos o valor do input
      const inputExer = document.getElementById('ValidExer' + (index + 1))
      // Verificamos se o botão está aparecendo
      const toggleExer = document.getElementById('toggleExer' + (index + 1))



      const btnSugest = document.getElementById('btnSugest')
      const titleSugest = document.getElementById('titleSugest')
      const categoryNull = document.getElementById('categoryNull')
      const sugest = document.getElementById('sugest')

      // Verifica se o exercicio de mesma categoria está vazio
      if (inputExer.value == "") {
        btnSugest.classList.add('d-none')
        sugest.classList.add('d-none')
        categoryNull.classList.add('d-none')

        titleSugest.innerHTML = `Sugerimos tentar fazer o <strong>${otherExerSameCategory.name}</strong> antes de fazer a troca desse exercicio`

      }
      // Se estiver preenchido e não for valido
      else {
        if (inputExer.value != "" && toggleExer.classList.contains('d-none')) {
          btnSugest.classList.add('d-none')
          categoryNull.classList.add('d-none')
          sugest.classList.remove('d-none')

          titleSugest.innerHTML = `Verificamos que você conseguiu fazer o ${otherExerSameCategory.name}. E este exercicio que você está tentando trocar é o de nivel 0 (Não tem exercicio mais fraco)`

          sugest.innerHTML = `Sugerimos que mantenha apenas com 1 exercicio da categoria ${otherExerSameCategory.category}`
        }
        // Se estiver preenchido e for valido
        else {

          btnSugest.classList.remove('d-none')
          sugest.classList.remove('d-none')


          titleSugest.innerHTML = `Verificamos que não conseguiu fazer os exercicios de NIVEL 0 da categoria <strong>${exerFound[0].category}</strong> (${otherExerSameCategory.name} e ${exerFound[0].name})</span>`


          sugest.innerHTML = 'Sugerimos mudar para <strong>Treino Hibrido</strong> ou <strong>Treino de Musculação</strong>'

        }
      }




      const zeroExer = document.getElementById('zeroExer')
      zeroExer.classList.remove('d-none')

      const zeroEcategoryNullxer = document.getElementById('categoryNull')
      zeroEcategoryNullxer.innerHTML = exerFound[0].category


    }
  }
  else {

    const divPai = document.getElementById('divToggle')
    divPai.innerHTML = ''
    var x = 1
    filterType.forEach(e => {
      // cria o primeiro elemento
      const div1 = document.createElement('div');
      div1.classList.add('row', 'reset-Padding', 'my-3');

      // cria o segundo elemento
      const div2s = document.createElement('div');
      div2s.classList.add('col-5', 'reset-Padding', 'd-flex', 'justify-content-center', 'align-items-center');

      // cria o terceiro elemento
      const img = document.createElement('img');
      img.setAttribute('width', '115');
      img.setAttribute('height', 'auto');
      img.setAttribute('src', e.url);

      // adiciona o terceiro elemento ao segundo elemento
      div2s.appendChild(img);

      // cria o quarto elemento
      const div3 = document.createElement('div');
      div3.classList.add('col-7', 'd-flex', 'align-items-center', 'reset-Padding');

      // cria o quinto elemento
      const div4 = document.createElement('div');
      div4.classList.add('row', 'reset-Padding');
      div4.id = 'row' + x
      // cria o sexto elemento
      const div5 = document.createElement('div');
      div5.classList.add('col-12', 'd-flex', 'justify-content-start', 'align-items-center', 'reset-Padding');

      // cria o sétimo elemento
      const span1 = document.createElement('span');
      span1.classList.add('reset');
      span1.textContent = e.name;

      // adiciona o sétimo elemento ao sexto elemento
      div5.appendChild(span1);

      // adiciona o sexto elemento ao quinto elemento
      div4.appendChild(div5);

      // cria o oitavo elemento
      const div6 = document.createElement('div');
      div6.classList.add('col-12', 'd-flex', 'justify-content-start', 'align-items-center', 'reset-Padding');

      // cria o nono elemento
      const span2 = document.createElement('span');
      span2.classList.add('reset');
      span2.textContent = `(${e.category} ${e.type})`;

      // adiciona o nono elemento ao oitavo elemento
      div6.appendChild(span2);

      // adiciona o oitavo elemento ao quinto elemento
      div4.appendChild(div6);

      // cria o décimo elemento
      const div7 = document.createElement('div');
      div7.classList.add('col-12', 'd-flex', 'justify-content-center', 'align-items-center', 'reset-Padding', 'W-100');

      // cria o décimo primeiro elemento
      const button = document.createElement('button');
      button.onclick = function () { subs(id, e.name, e.category, e.type, e.url, e.nivel) };
      button.id = 'toggle' + x
      button.className = 'btn btn-primary mt-2';
      button.innerText = 'Trocar';
      button.classList.add('btn', 'btn-primary', 'mt-2');
      button.setAttribute('data-bs-dismiss', 'modal');
      button.setAttribute('style', 'width: 100%');
      button.textContent = 'Trocar';

      // adiciona o décimo primeiro elemento ao décimo elemento
      div7.appendChild(button);

      // adiciona o quinto e o décimo elemento ao quarto elemento
      div4.appendChild(div5);
      div4.appendChild(div6);
      div4.appendChild(div7);

      // adiciona o segundo e o quarto elemento ao terceiro elemento
      div3.appendChild(div4);

      // adiciona o segundo e o terceiro elemento ao primeiro elemento
      div1.appendChild(div2s);
      div1.appendChild(div3);

      // adiciona o primeiro elemento ao elemento pai
      divPai.appendChild(div1);
      x++
    })

  }

}

function subs(id, name, category, type, img, nivel) {
  const Name = document.getElementById('ValidTitle' + id)
  const Img = document.getElementById('img' + id)
  const div = document.getElementById('toggleExer' + id)
  const input = document.getElementById('ValidExer' + id)
  const repts = document.getElementById('repts' + id)

  // var newArray = []
  // newExercisesBase.forEach(e => {
  //   if (e == undefined) {
  //     return
  //   }
  //   newArray.push(e)
  // })

  var nameExer = exercises.filter(e => e.name == name)
  // Subistituir no array
  let indexExer = newExercisesBase.findIndex(e => e.name == Name.innerHTML)
  if (indexExer != -1) {
    newExercisesBase[indexExer] = nameExer[0]
  }

  if (nameExer[0].segs) {
    repts.innerHTML = 'SEGS'
  }
  else {
    repts.innerHTML = 'REPS'
  }

  // zerar a div do botão
  div.innerHTML = ''

  div.innerHTML = `<button id="${'btn' + id}" onclick="filter(${id}, '${name}', '${category}', '${type}', ${nivel})" class="btn btn-primary mb-2 w-100" data-bs-toggle="modal" data-bs-target="#exampleModal">Trocar Exercicío</button>
  <span id="${'heavy' + id}" class="reset text-danger text-start px-2 d-none" style="font-size: 10px;">
  *Ops, sua quantidade de ${nameExer[0].segs ? 'segundos' : 'repetição'} está baixa! Vamos trocar para um mais leve?
  </span>

  <span id="${'light' + id}" class="reset text-danger text-start px-2 d-none" style="font-size: 10px;">
    *Ops, sua quantidade de ${nameExer[0].segs ? 'segundos' : 'repetição'} está alta! Vamos trocar para um mais pesado?
  </span> 

  </div>
  <span id="${'success' + id}" class="reset px-3 text-start text-success d-none" style="font-size: 10px;">
  Perfeito, agora é só descansar ${nameExer[0].rest}m e fazer o próximo exercício
  </span> 
  `

  // Trocando o exercicio
  Name.innerHTML = name
  Img.src = img

  // Esconde o button
  const btn = document.getElementById('toggleExer' + id)
  btn.classList.add('d-none')
  btn.classList.remove('d-block')

  // Zerar input
  input.value = ''

  input.classList.remove('text-danger')
  input.classList.remove('input-exer')
  input.classList.remove('input-danger')
  input.classList.remove('input-exer-fail')

  input.classList.add('input-exer')
  input.classList.add('input-value')

  repts.classList.remove('text-danger')
  repts.classList.add('text-gray1')


}

function openToggleExer(id, Title, Input, bool) {
  const input = document.getElementById('ValidExer' + id);
  const btn = document.getElementById('toggleExer' + id)
  const light = document.getElementById('light' + id)
  const heavy = document.getElementById('heavy' + id)
  const repts = document.getElementById('repts' + id)
  const success = document.getElementById('success' + id)
  const noInput = document.getElementById('noInput' + id)

  var exer = exercises.filter(e => e.name == Title.innerHTML)
  // Se for segs
  if (exer[0].segs) {
    // Se o exercicio nao for de segundos ira executar essa validação

    let segundos = input.value / 2 //Resposta em segundos
    let repeticao = 60 / Math.round(segundos) // Repostas em repetição
    repeticao = Math.round(repeticao)
    let sugundosTotais = segundos * repeticao // Segundos totais do exer

    // Dentro dos parametros
    if (repeticao <= 4 && input.value < 60) {
      // if (bool) {
      noInput.classList.add('d-none')
      success.classList.remove('d-none')
      // Tempo da message de sucesso
      setTimeout(function () {
        success.classList.add("d-none");
      }, 180000);
      // }
      input.classList.remove('text-danger')
      input.classList.remove('input-danger')

      repts.classList.remove('text-danger')
      repts.classList.add('text-gray1')

      btn.classList.add('d-none')
      btn.classList.remove('d-block')

      let card = parseInt(id)
      // desabilitCard(card)
      gerarTreino(Title, Input, id)
    }
    // Se o numero de repetição for 5 ou 6 mostra o modal
    if (repeticao == 5 || repeticao == 6) {
      noInput.classList.add('d-none')
      //  dar opção de eliminar exercicio
      var modal = new bootstrap.Modal(document.querySelector('#toggleExerSegs'));

      // Pegar nome do exer que ira ser deletado
      let exerRemove = newExercisesBase.filter(e => e.category == exer[0].category && e.name != exer[0].name)

      // Imprimir na tela
      const exerDeletr = document.getElementById('exerDeleter')
      exerDeletr.innerHTML = exerRemove[0].name

      // Imprimir nome do exercicio que está pesado
      const name = document.getElementById('nameExer')
      name.innerHTML = exer[0].name



      var fixArray = []
      newExercisesBase.forEach(e => {
        if (e == undefined) {
          return
        }
        fixArray.push(e)
      })

      var countCategory = fixArray.filter(e => e.category == exer[0].category)

      if (countCategory.length == 1) {
        // Mostra o botão de trocar o exercicio
        btn.classList.add('d-block')
        btn.classList.remove('d-none')
      }
      else {
        // filtra por categori e pega o outro exercicio da mesma catagoria
        let exerRemove = newExercisesBase.filter(e => e.category == exer[0].category && e.name != exer[0].name)

        btn.classList.add('d-none')

        const btnremove = document.getElementById('removeExer')
        btnremove.onclick = function () { removeExer(exerRemove, id, Title, Input, exer) };

        // Exibir o modal
        modal.show();

        const notRemove = document.getElementById('notRemove')
        notRemove.onclick = function () { showBtn(btn) }
      }

    }
    // Se for maior que 6 mostra messagem de erro PESADO
    if (repeticao > 6 || input.value >= 60) {
      noInput.classList.add('d-none')
      // Texto de sucesso some
      success.classList.add('d-none')

      // Mostra o botão de trocar o exercicio
      btn.classList.add('d-block')
      btn.classList.remove('d-none')

      //Mostra a obs de exer leve
      light.classList.add('d-block')
      light.classList.remove('d-none')

      //Oculta a obs de exer pesado
      heavy.classList.add('d-none')
      heavy.classList.remove('d-block')

      //Add visuald e erro
      input.classList.add('text-danger')
      input.classList.add('input-danger')

      repts.classList.add('text-danger')
      repts.classList.remove('text-gray1')
    }
    // Leve
    if (repeticao < 2) {
      noInput.classList.add('d-none')
      // Texto de sucesso some
      success.classList.add('d-none')

      // Mostra o botão de trocar o exercicio
      btn.classList.add('d-block')
      btn.classList.remove('d-none')

      //Mostra a obs de exer leve
      light.classList.add('d-block')
      light.classList.remove('d-none')

      //Oculta a obs de exer pesado
      heavy.classList.add('d-none')
      heavy.classList.remove('d-block')

      //Add visuald e erro
      input.classList.add('text-danger')
      input.classList.add('input-danger')

      repts.classList.add('text-danger')
      repts.classList.remove('text-gray1')
    }


  }
  // Se for repts
  else {
    if (exer[0].name == 'Dips na paralela' || exer[0].name == 'Pull Ups') {
      if (input.value <= 3) {
        noInput.classList.add('d-none')
        // Texto de sucesso some
        success.classList.add('d-none')

        // Mostra o botão de trocar o exercicio
        btn.classList.add('d-block')
        btn.classList.remove('d-none')

        //Mostra a obs de exer pesado
        heavy.classList.add('d-block')
        heavy.classList.remove('d-none')

        //Oculta a obs de exer leve
        light.classList.add('d-none')
        light.classList.remove('d-block')

        //Add visuald e erro
        input.classList.add('text-danger')
        input.classList.add('input-danger')

        repts.classList.add('text-danger')
        repts.classList.remove('text-gray1')

      }
      if (input.value > 3 && input.value < 16) {

        let card = parseInt(id)
        // desabilitCard(card)

        noInput.classList.add('d-none')
        if (bool) {
          success.classList.remove('d-none')
          // Tempo da message de sucesso
          setTimeout(function () {
            success.classList.add("d-none");
          }, 180000);
        }
        input.classList.remove('text-danger')
        input.classList.remove('input-danger')

        repts.classList.remove('text-danger')
        repts.classList.add('text-gray1')

        btn.classList.add('d-none')
        btn.classList.remove('d-block')
        gerarTreino(Title, Input, id)

        const divPai = document.getElementById('divToggle')
        divPai.innerHTML = ''
        if (treino.length === 8) {
          // fechar model
          // const button = document.getElementById('saveTraining')
          // button.setAttribute('data-bs-dismiss', 'modal')
        }
      }
      if (input.value > 15) {
        noInput.classList.add('d-none')
        // Texto de sucesso some
        success.classList.add('d-none')

        // Mostra o botão de trocar o exercicio
        btn.classList.add('d-block')
        btn.classList.remove('d-none')

        //Mostra a obs de exer leve
        light.classList.add('d-block')
        light.classList.remove('d-none')

        //Oculta a obs de exer pesado
        heavy.classList.add('d-none')
        heavy.classList.remove('d-block')

        //Add visuald e erro
        input.classList.add('text-danger')
        input.classList.add('input-danger')

        repts.classList.add('text-danger')
        repts.classList.remove('text-gray1')
      }
    }
    else {
      if (input.value < 6) {
        noInput.classList.add('d-none')

        // Texto de sucesso some
        success.classList.add('d-none')

        // Mostra o botão de trocar o exercicio
        btn.classList.add('d-block')
        btn.classList.remove('d-none')

        //Mostra a obs de exer pesado
        heavy.classList.add('d-block')
        heavy.classList.remove('d-none')

        //Oculta a obs de exer leve
        light.classList.add('d-none')
        light.classList.remove('d-block')

        //Add visuald e erro
        input.classList.add('text-danger')
        input.classList.add('input-danger')

        repts.classList.add('text-danger')
        repts.classList.remove('text-gray1')

      }
      if (input.value > 5 && input.value < 16) {

        let card = parseInt(id)
        // desabilitCard(card)
        noInput.classList.add('d-none')
        if (bool) {
          success.classList.remove('d-none')
          let divExer = document.getElementById('exer' + id)
          // Tempo da message de sucesso
          setTimeout(function () {
            success.classList.add("d-none");
          }, 180000);
        }


        input.classList.remove('text-danger')
        input.classList.remove('input-danger')

        repts.classList.remove('text-danger')
        repts.classList.add('text-gray1')

        btn.classList.add('d-none')
        btn.classList.remove('d-block')
        gerarTreino(Title, Input, id)

        const divPai = document.getElementById('divToggle')
        divPai.innerHTML = ''
        if (treino.length === 8) {
          // fechar model
          // const button = document.getElementById('saveTraining')
          // button.setAttribute('data-bs-dismiss', 'modal')
        }
      }
      if (input.value > 15) {
        // Texto de sucesso some
        noInput.classList.add('d-none')
        success.classList.add('d-none')

        // Mostra o botão de trocar o exercicio
        btn.classList.add('d-block')
        btn.classList.remove('d-none')

        //Mostra a obs de exer leve
        light.classList.add('d-block')
        light.classList.remove('d-none')

        //Oculta a obs de exer pesado
        heavy.classList.add('d-none')
        heavy.classList.remove('d-block')

        //Add visuald e erro
        input.classList.add('text-danger')
        input.classList.add('input-danger')

        repts.classList.add('text-danger')
        repts.classList.remove('text-gray1')
      }
    }
  }


}

function addColorError() {
  for (let i = 1; i < newExercisesBase.length + 1; i++) {
    const input = document.getElementById('ValidExer' + i)
    const title = document.getElementById('ValidTitle' + i)
    const repts = document.getElementById('repts' + i)
    const light = document.getElementById('light' + i)
    const heavy = document.getElementById('heavy' + i)
    const noInput = document.getElementById('noInput' + i)


    if (input.value == NaN || input.value == null || input.value == undefined || input.value == "") {
      // Se o input estiver vazio add as classes 
      input.classList.remove('input-exer')
      input.classList.add('input-exer-fail')
      repts.classList.add('text-danger')

      // setTimeout(function () {
      noInput.classList.remove('d-none')
      // }, 180000);
    } else {
      // Se estiver preenchido
      noInput.classList.add('d-none')
      input.classList.add('input-exer')
      input.classList.remove('input-exer-fail')
      repts.classList.remove('text-danger')
      // title.classList.remove('text-danger')

      openToggleExer(i, title, input, false)
    }

  }
}

function removeColorError() {
  const input = document.getElementById('ValidExer' + id)
  const title = document.getElementById('ValidTitle' + id)
  const repts = document.getElementById('repts' + id)

  input.classList.add('input-exer')
  input.classList.remove('input-exer-fail')
  repts.classList.remove('text-danger')
  title.classList.remove('text-danger')
}

function creatStruct(id) {
  const input = document.getElementById('ValidExer' + id)
  const title = document.getElementById('ValidTitle' + id)
  const repts = document.getElementById('repts' + id)

  input.addEventListener('blur', function () {
    if (input.value == NaN ||
      input.value == null ||
      input.value == undefined ||
      input.value == "") {

      input.classList.remove('input-exer')
      input.classList.add('input-exer-fail')
      repts.classList.add('text-danger')
    } else {
      repts.classList.remove('text-danger')
      input.classList.remove('input-exer-fail')
      input.classList.add('input-exer')
      openToggleExer(id, title, input, true)
    }
  })
}

function gerarTreino(title, input, id) {
  // Cria um novo objeto com as informações do exercício
  const exer = getImgUrl(title.innerHTML)
  let novoExercicio = {}
  var valueInput = parseInt(input.value)

  let exerFound = exercises.filter(e => e.name == title.innerHTML)[0]

  let segundos = Math.round(valueInput / 2)//Resposta em segundos
  let repeticao = Math.round(60 / segundos) // Repostas em repetição


  if (exerFound.segs) {
    // add no treino, com as regras de segundos
    novoExercicio = { name: title.innerHTML, count: segundos, rept: repeticao, rest: 3, url: exer, num: id, segs: "true" };
  }
  else {
    if (title.innerHTML == "Dips na paralela" || title.innerHTML == "Pull Ups") {

      if (valueInput == 3 || valueInput == 4 || valueInput == 5) {
        if (valueInput == 3) {
          novoExercicio = { name: title.innerHTML, count: (valueInput - 1), rept: 5, rest: 3, url: exer, num: id };
        }
        if (valueInput == 4) {
          novoExercicio = { name: title.innerHTML, count: (valueInput - 1), rept: 5, rest: 3, url: exer, num: id };
        }
        if (valueInput == 5) {
          novoExercicio = { name: title.innerHTML, count: (valueInput - 1), rept: 4, rest: 3, url: exer, num: id };
        }
      }
      else {
        novoExercicio = { name: title.innerHTML, count: (valueInput - 1), rept: 3, rest: 3, url: exer, num: id };
      }
    }
    else {
      novoExercicio = { name: title.innerHTML, count: (valueInput - 1), rept: 3, rest: 3, url: exer, num: id };
    }
  }

  const found = treino.findIndex(e => e.name == novoExercicio.name)
  if (found !== -1) {

    if (exerFound.segs) {
      // add no treino, com as regras de segundos
      treino[found].rept = repeticao
      treino[found].count = segundos
    }
    else {
      if (treino[found].name == "Dips na paralela" || treino[found].name == "Pull Ups") {

        if (valueInput == 3 || valueInput == 4 || valueInput == 5) {
          if (valueInput == 3) {
            treino[found].rept = 5
            treino[found].count = (valueInput - 1)
          }
          if (valueInput == 4) {
            treino[found].rept = 5
            treino[found].count = (valueInput - 1)
          }
          if (valueInput == 5) {
            treino[found].rept = 4
            treino[found].count = (valueInput - 1)
          }
        }
        else {
          treino[found].rept = 3
          treino[found].count = (valueInput - 1)
        }
      }
      else {
        treino[found].rept = 3
        treino[found].count = (valueInput - 1)
      }
    }
  } else {
    treino.push(novoExercicio);
    console.log(treino)
  }
}

function validationQtdExer() {
  var filterCategory = []

  treino.forEach(e => {
    var aux = exercises.filter(i => i.name == e.name)
    filterCategory.push(aux)
  })

  var Push = filterCategory.flat().filter(e => e.category == 'Push')
  var Pull = filterCategory.flat().filter(e => e.category == 'Pull')
  var Core = filterCategory.flat().filter(e => e.category == 'Core')
  var Legs = filterCategory.flat().filter(e => e.category == 'Legs')

  if (Push.length == 1) {
    // Procura no treino qual é o index do exercicio que precisa ser alterado
    let indexName = treino.findIndex(e => e.name == Push[0].name)
    // Atualiza o count = 5 e rept = (total -2)
    if (indexName !== -1) {
      treino[indexName].rept = 5
      treino[indexName].count -= 1
    } else {
    }
  }

  if (Pull.length == 1) {
    // Procura no treino qual é o index do exercicio que precisa ser alterado
    let indexName = treino.findIndex(e => e.name == Pull[0].name)
    // Atualiza o count = 5 e rept = (total -2)
    if (indexName !== -1) {
      treino[indexName].rept = 5
      treino[indexName].count -= 1
    } else {
    }
  }

  if (Core.length == 1) {
    // Procura no treino qual é o index do exercicio que precisa ser alterado
    let indexName = treino.findIndex(e => e.name == Core[0].name)
    // Atualiza o count = 5 e rept = (total -2)
    if (indexName !== -1) {
      treino[indexName].rept = 5
      treino[indexName].count -= 1
    } else {
    }
  }

  if (Legs.length == 1) {
    // Procura no treino qual é o index do exercicio que precisa ser alterado
    let indexName = treino.findIndex(e => e.name == Legs[0].name)
    // Atualiza o count = 5 e rept = (total -2)
    if (indexName !== -1) {
      treino[indexName].rept = 5
      treino[indexName].count -= 1
    } else {
    }
  }


}

function removeExer(exer, id, Title, Input, exerRestante) {
  // Remove o exercicio do array

  var treino2 = []
  newExercisesBase.forEach(e => {
    if (e == undefined) {
      return
    }
    treino2.push(e)
  })

  let index = treino2.findIndex(e => e.name === exer[0].name);
  if (index !== -1) {
    treino2.splice(index, 1); //remova o elemento com o índice encontrado
  }

  let treinoDel = treino.findIndex(e => e.name === exer[0].name)
  if (treinoDel !== -1) {
    treino.splice(treinoDel, 1); //remova o elemento com o índice encontrado
  }
  // ---------------------------------------------------------------------
  // remove visualmente o exer
  var x = 1
  newExercisesBase.forEach(e => {
    if (e == undefined) {
      return
    }
    if (e.name == exer[0].name) {
      const divRemove = document.getElementById('exer' + x)
      divRemove.remove()
    }
    x++
  })
  newExercisesBase = treino2
  if (Title) {
    gerarTreino(Title, Input, id)
  }

  if (exerRestante) {
    let index = newExercisesBase.findIndex(e => e.name == exerRestante[0].name)

    let input = document.getElementById('ValidExer' + (index + 1))
    input.classList.remove('input-danger')
    input.classList.remove('text-danger')
  }
  return newExercisesBase; //retorne o array atualizado
}

function openModal(id) {
  var modal = new bootstrap.Modal(document.querySelector(`#${id}`));
  modal.show()
}

function showBtn(btn) {
  btn.classList.add('d-block')
  btn.classList.remove('d-none')
}

function correctingArray(treino, exercicio) {
  let data_all = [];

  exercicio.forEach(a => {
    treino.forEach(t => {
      if (a["name"] == t["name"]) {
        let new_data = Object.assign({}, a, t);
        data_all.push(new_data);
      }
    });
  });
  return data_all
}

function desabilitCard(id) {

  // Monta o array de id sem o id que está sendo tratado
  let cardAtual = numberInput.findIndex(e => e == id)
  if (cardAtual != -1) {
    numberInput.splice(cardAtual, 1);
  }
  // Desabilita todos os inpust e add uma class aos cards
  numberInput.forEach(e => {
    const inputDesabilit = document.getElementById('ValidExer' + e)
    inputDesabilit.disabled = true;
    const divExer = document.getElementById('exer' + e)
    divExer.classList.add('desabilited')
  })

  let meuInput = document.getElementById('ValidExer' + id);
  let cronometro = document.getElementById("cronometro");
  let segundosRestantes = 180; // 3 minutos em segundos
  let interval; // Declarando a variável fora da função para poder usar em outro escopo


  clearInterval(interval); // Parar o cronômetro se ele já estiver rodando
  segundosRestantes = 180; // Reiniciar o tempo

  interval = setInterval(function () {
    segundosRestantes--;
    let minutos = Math.floor(segundosRestantes / 60);
    let segundos = segundosRestantes % 60;
    cronometro.innerHTML = minutos + "m " + segundos + "s";

    if (segundosRestantes <= 0) {
      clearInterval(interval); // Parar o cronômetro
      meuInput.disabled = false; // Habilitar input
      cronometro.innerHTML = "fim";

      numberInput.forEach(e => {
        const inputDesabilit = document.getElementById('ValidExer' + e)
        inputDesabilit.disabled = false;
        const divExer = document.getElementById('exer' + e)
        divExer.classList.remove('desabilited')
      })
    }
  }, 1000); // Atualizar o cronômetro a cada segundo

}

function loading(x) {
  if (x == true) {
    document.getElementById('body-content').classList.add('d-none');
    document.getElementById('loading').classList.remove('d-none');
  }
  else {
    document.getElementById('body-content').classList.remove('d-none');
    document.getElementById('loading').classList.add('d-none');
  }
}

// ----------------------------------------------------------- Page firstAcess.html
// Obtém o elemento do carrossel e seus itens internos
const quizCarousel = document.querySelector('#quiz');
const quizItems = quizCarousel.querySelectorAll('.carousel-item');
const hours = document.getElementById('hours')
const min = document.getElementById('min')
const days = document.getElementById('days')

const timeErr = document.getElementById('timeErr')

// Percorre cada item do quiz e adiciona um evento de clique em seus inputs de opção
quizItems.forEach(item => {
  const optionInputs = item.querySelectorAll('.form-check-input');

  optionInputs.forEach((input) => {
    input.addEventListener('click', () => {
      const name = input.name
      const value = input.value
      const index = requireds.findIndex((e) => e.name == name)

      // Verificação se já existe o item no array
      if (index !== -1) {
        requireds[index].value = value
      } else {
        requireds.push({ name: name, value: value })
      }

      if (requireds.length == 6 && input.name != 'qtdTreino') {
        $('input[type=radio]').change(function () {
          $('.carousel').carousel('next'); // Avança para o próximo slide
        });

        if (requireds.length > 6) {
          // console.log('wee')
        }
      }
    });
  });
});

days.addEventListener('change', function () {
  var D = parseInt(days.value)
  if (D <= 0) {
    // Erro de dia
  }
  else {
    var newData = { name: 'days', value: days.value }
    requireds.push(newData)
  }
})

hours.addEventListener('change', function () {
  var H = parseInt(hours.value)
  var M = parseInt(min.value)

  min.classList.remove('selecte-err')
  hours.classList.remove('selecte-err')

  const index = requireds.findIndex((e) => e.name == 'hours')
  const indexMin = requireds.findIndex((e) => e.name == 'min')

  // Verificação se já existe o item no array
  if (index !== -1) {
    requireds[index].value = hours.value
    if (indexMin !== -1) {
      requireds[indexMin].value = min.value
    }
  } else {
    requireds.push({ name: 'hours', value: hours.value })
  }

  //Da um filter no array em busca dos minutos
  var find = requireds.filter(e => e.min != 'Min.')
  // Se não tiver minutos no arrai nao cria os exercicios
  if (find.length >= 9) {
    verificationRequireds()
  }

})

min.addEventListener('change', function () {
  var M = parseInt(min.value)
  var H = parseInt(hours.value)
  const index2 = requireds.findIndex((e) => e.min == min.value)

  if (M <= 39 && H <= 0) {
    //Lógica do erro
    min.classList.add('selecte-err')
    hours.classList.add('selecte-err')
    timeErr.classList.remove('d-none')
    if (index2 !== -1) {
      requireds[index2].value = min.value
    } else {
      requireds.push({ name: 'min', value: min.value })
    }
  }
  else {
    timeErr.classList.add('d-none')
    // Verifica se já existe, se tiver att se nao adiciona
    if (index2 !== -1) {
      requireds[index2].value = min.value
    } else {
      requireds.push({ name: 'min', value: min.value })
    }

    //Da um filter no array em busca das horas
    var find = requireds.filter(e => e.hours != 'horas')
    // Se não tiver horas no arrai nao cria os exercicios
    if (find.length >= 9) {
      verificationRequireds()
    }
  }
})

function verificationRequireds() {
  var superband = requireds.filter(e => e.name == 'superband')[0].value
  var paralelas = requireds.filter(e => e.name == 'paralelas')[0].value
  var barraFixa = requireds.filter(e => e.name == 'barraFixa')[0].value
  var argolas = requireds.filter(e => e.name == 'argolas')[0].value
  var trx = requireds.filter(e => e.name == 'trx')[0].value
  var rodinha = requireds.filter(e => e.name == 'rodinha')[0].value
  var days = parseInt(requireds.filter(e => e.name == 'days')[0].value)
  var horas = requireds.filter(e => e.name == 'hours')[0]
  var min = requireds.filter(e => e.name == 'min')[0]

  // Add os sem filtros
  var aux = exercises.filter(e => e.required == "")
  aux.forEach(e => {
    newExercises.push(e)
  })


  if (superband == 'true') {
    var aux = exercises.filter(e => {
      if (Array.isArray(e.required)) {
        return e.required.includes('superband');
      } else {
        return e.required == 'superband';
      }
    });
    aux.forEach(e => {
      newExercises.push(e)
    });
  }
  if (paralelas == 'true') {
    var aux = exercises.filter(e => {
      if (Array.isArray(e.required)) {
        return e.required.includes('paralelas');
      } else {
        return e.required == 'paralelas';
      }
    });
    aux.forEach(e => {
      newExercises.push(e)
    });
  }
  if (barraFixa == 'true') {
    var aux = exercises.filter(e => {
      if (Array.isArray(e.required)) {
        return e.required.includes('barraFixa');
      } else {
        return e.required == 'barraFixa';
      }
    });
    aux.forEach(e => {
      newExercises.push(e)
    });
  }
  if (argolas == 'true') {
    var aux = exercises.filter(e => {
      if (Array.isArray(e.required)) {
        return e.required.includes('argolas');
      } else {
        return e.required == 'argolas';
      }
    });
    aux.forEach(e => {
      newExercises.push(e)
    });
  }
  if (trx == 'true') {
    var aux = exercises.filter(e => {
      if (Array.isArray(e.required)) {
        return e.required.includes('trx');
      } else {
        return e.required == 'trx';
      }
    });
    aux.forEach(e => {
      newExercises.push(e)
    });
  }
  if (rodinha == 'true') {
    var aux = exercises.filter(e => {
      if (Array.isArray(e.required)) {
        return e.required.includes('rodinha');
      } else {
        return e.required == 'rodinha';
      }
    });
    aux.forEach(e => {
      newExercises.push(e)
    });
  }

  // Verifica se tem o minimo 
  if (paralelas == 'false' && barraFixa == 'false' && argolas == 'false' && trx == 'false') {
    const quiz = document.getElementById('quiz')
    quiz.classList.add('d-none')

    const divErr = document.getElementById('msgErr')
    divErr.classList.remove('d-none')
  }
  else {

    // Primeiro Exercicio
    paralelas == 'true' ?
      newExercisesBase.push(exercises.filter(e => e.name == 'Dips na paralela')[0]) :
      newExercisesBase.push(newExercises.filter(e => e.nivel == 2 && e.type == 'Vertical' && e.category == 'Push')[0])

    // Segundo Exercicio
    newExercisesBase.push(newExercises.filter(e => e.name == 'Flexão Padrão')[0])

    // Terceiro Exercicio
    barraFixa == 'true' ?
      newExercisesBase.push(exercises.filter(e => e.name == 'Pull Ups')[0]) :
      newExercisesBase.push(newExercises.filter(e => e.nivel == 3 && e.type == 'Vertical' && e.category == 'Pull')[0])

    // Quarto Exercicio
    newExercisesBase.push(exercises.filter(e => e.name == 'Rows/Barra Australiana')[0])

    // Quinto Exercicio
    newExercisesBase.push(exercises.filter(e => e.name == 'Full Squat (descer tudo)')[0])

    // Sexto Exercicio
    newExercisesBase.push(exercises.filter(e => e.name == 'Hip Thruster')[0])

    // Setimo Exercicio
    paralelas == 'true' ?
      newExercisesBase.push(exercises.filter(e => e.name == 'Tuck L-sit')[0]) :
      newExercisesBase.push(newExercises.filter(e => e.nivel == 2 && e.type == 'Abdômen' && e.category == 'Core')[0])

    // Oitavo Exercicio
    newExercisesBase.push(exercises.filter(e => e.name == '60s de Prancha Abdominal')[0])

    creatExercisesBase()
  }
}

// Desativa a rotação automática do carrossel
quizCarousel.setAttribute('data-bs-interval', 'false');


// ----------------------------------------------------------- Page Home2.html

function chosenRoutine(rotina) {
  if (rotina == 'Fullbody') {
    const Fullbody = document.getElementById('Fullbody')
    Fullbody.classList.remove('d-none')
  }
  if (rotina == 'PushPull') {
    const PushPull = document.getElementById('PushPull')
    PushPull.classList.remove('d-none')
  }
  if (rotina == 'UpperLower') {
    const UpperLower = document.getElementById('UpperLower')
    UpperLower.classList.remove('d-none')
  }

  const text1 = document.getElementById('text1')
  const text2 = document.getElementById('text2')
  text1.classList.add('d-none')
  text2.classList.add('d-none')

  const bntPdf = document.getElementById('bntPdf')
  bntPdf.classList.remove('d-none')

  fetch('/saveTraining', {
    method: 'POST',
    body: rotina,
    headers: {
      'Content-Type': 'application/json'
    }
  })
    .then(response => {
      console.log(response)
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Erro na requisição:', response.status);
      }
    })
    .then(data => {
      console.log(data.message);
    })
    .catch(error => {
      console.error(error);
    });
}

// ----------------------------------------------------------- Page exercices.html
function loadExer() {
  const listFilter = document.getElementById('listFilter')
  let div = listFilter.innerHTML
  exercises.forEach(e => {
    div += `
    <div onclick="openDetailExer()" class="row my-2">
    <div class="col-12 mt-3 reset-Padding-x">
        <h2>${e.name}</h2>
    </div>

    <div class="col-4 d-flex justify-content-start align-items-center rounded-4 reset-Padding-x">
        <img class="rounded-4 img-res" id="img1" width="100" height="100"
            src="${e.url}" alt="">
    </div>

    <div class="col-8 d-flex flex-column justify-content-around align-items-start">
        <span class="reset text-start"> Informações</span>

        <div class="d-flex  justify-content-center align-items-start gap-2">
            <span class="text-start">Equipamentos:</span>
            <span>${e.required}</span>
        </div>

        <div class="d-flex justify-content-center align-items-start gap-2">
            <span class="text-start">Grupo Muscular:</span>
            <span>${e.category}</span>
        </div>

        <div class="d-flex justify-content-center align-items-start gap-2">
            <span class="text-start">Nivel:</span>
            <span>${e.nivel}</span>
        </div>

    </div>
</div>
    `
  })
  listFilter.innerHTML += div
}

function openDetailExer() {
  const filterPage = document.getElementById('filterPage')
  const listFilter = document.getElementById('listFilter')
  const page = document.getElementById('page')
  filterPage.classList.add('d-none')
  listFilter.classList.add('d-none')
  page.classList.remove('d-none')
}

function backPage() {
  const filterPage = document.getElementById('filterPage')
  const listFilter = document.getElementById('listFilter')
  const page = document.getElementById('page')
  filterPage.classList.remove('d-none')
  listFilter.classList.remove('d-none')
  page.classList.add('d-none')
}

function filterPage(data) {
  const listFilter = document.getElementById('listFilter')
  listFilter.innerHTML = ''
  let div = listFilter.innerHTML
  data.forEach(e => {
    div += `
    <div onclick="openDetailExer()" class="row my-2 max-height">
    <div class="col-12 mt-3 reset-Padding-x">
        <h2>${e.name}</h2>
    </div>

    <div class="col-4 d-flex justify-content-start align-items-center rounded-4 reset-Padding-x">
        <img class="rounded-4 img-res" id="img1" width="100" height="100"
            src="${e.url}" alt="">
    </div>

    <div class="col-8 d-flex flex-column justify-content-around align-items-start">
        <span class="reset text-start"> Informações</span>

        <div class="d-flex  justify-content-center align-items-start gap-2">
            <span class="text-start">Equipamentos:</span>
            <span>${e.required}</span>
        </div>

        <div class="d-flex justify-content-center align-items-start gap-2">
            <span class="text-start">Grupo Muscular:</span>
            <span>${e.category}</span>
        </div>

        <div class="d-flex justify-content-center align-items-start gap-2">
            <span class="text-start">Nivel:</span>
            <span>${e.nivel}</span>
        </div>

    </div>
</div>
    `
  })
  listFilter.innerHTML += div
}

// ------------------------------------------------------------- Ultima função
async function enviarTreino2() {
  if (treino.length == newExercisesBase.length) {
    //Enviando o valor de Paired Sets
    const pairedSets = document.getElementById('pairedSetsValue').checked
    var stre = ""
    pairedSets ? stre = "true" : stre = "false"
    const newAtt = { name: "Paired Sets", value: stre }
    treino.push(newAtt)

    let res = requireds.filter(e => e.name == 'days')[0]
    let days = parseInt(res.value)
    let newData = { name: 'days', value: days }
    treino.push(newData)

    debugger
   

    loading(true)
    try {
      const response = await fetch('/sendTraining', {
        method: 'POST',
        body: JSON.stringify(treino),
        headers: {
          'Content-Type': 'application/json'
        }
      });

      if (response.redirected) {
        window.location.replace(response.url);
      } else {
        loadExer(false)
      }
    } catch (error) {
      console.error('Erro na requisição:', error);
      // Esconde a animação de carregamento
      loadExer(false)
    }

  } else {
    addColorError()
  }


}