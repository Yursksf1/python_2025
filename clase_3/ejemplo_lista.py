# calcular promedios 
notas = [95, 70, 100, 25, 100, 50]
suma_notas = 0
count = 0
for nota in notas:
    count = count + 1
    suma_notas = suma_notas + nota

promedio = suma_notas/len(notas)
print('promedio', promedio )


# contador de caracteres 
texto = """
Colombia, oficialmente República de Colombia, es un país soberano situado en la región noroccidental de América del Sur. Se constituye en un Estado unitario, social y democrático de derecho, cuya forma de gobierno es de República presidencialista; con dos cámaras legislativas (Cámara de Representantes y Senado), también por sufragio directo, voluntario y secreto, con 4 años de mandato, pero que en cambio sí pueden ser reelegidos. Su capital y ciudad más poblada es Bogotá.12​ Es una república organizada políticamente en treinta y dos departamentos descentralizados y el Distrito Capital de Bogotá,13​ sede del Gobierno nacional.

Incluyendo la isla de Malpelo, el cayo Roncador y el banco Serrana, el país abarca una superficie de 1 141 748 km²,3​ por lo que es el vigesimoquinto país más grande del mundo y el séptimo más grande de América. Reclama como mar territorial el área hasta las 12 millas náuticas de distancia,4​ manteniendo un diferendo limítrofe al respecto con Venezuela y Nicaragua.14​15​

Limita al norte, con el océano Atlántico; al este, con Venezuela y Brasil; al sur con Perú y Ecuador; y al oeste, con el océano Pacífico y Panamá.16​ Tiene costas en el océano Pacífico y acceso al Atlántico a través del mar Caribe,17​ donde posee diversas islas como el archipiélago de San Andrés, Providencia y Santa Catalina.18​

Es el vigesimoséptimo país más poblado del mundo, con una población de 52 millones de habitantes,19​ además es la segunda nación con más hispanohablantes, detrás de México.20​ Posee una población multicultural, la cual refleja la influencia de la colonización europea a gran escala, pueblos nativos y mano de obra africana, con oleadas migratorias provenientes de Europa21​22​23​24​ y Oriente Medio25​26​27​28​ durante los siglos XIX y XX.29​30​31​

El producto interno bruto de paridad de poder adquisitivo de Colombia ocupa el cuarto puesto en América Latina y el puesto 28 a nivel mundial. El PIB nominal colombiano es el cuarto más grande de América Latina y ocupa el puesto 28 a nivel mundial.32​

La presencia humana en Colombia se remonta a más de 14 500 años.33​34​35​ Después de miles de años de formación cultural, en el actual territorio colombiano surgieron diversas culturas precolombinas como los muiscas, taironas y quimbayas. Al colonizar a estas culturas, España creó el Virreinato de la Nueva Granada con capital en Santafé (hoy Bogotá).

En el año 1810 comenzó la Guerra de independencia, tras la cual surgió el país que actualmente se conoce como Colombia. Durante el siglo xix y el siglo xx, el país se caracterizó por su inestabilidad y un gran número de guerras civiles;36​ el último de estos conflictos, conocido como conflicto armado interno, comenzó en 1960. En el año 2012, después de más cincuenta años de conflicto, el gobierno del entonces presidente Juan Manuel Santos inició conversaciones de paz con las FARC-EP. En 2016 se alcanzó un acuerdo final que a pesar de no ser aprobado en el plebiscito del 2 de octubre del mismo año, fue implementado con modificaciones en 2017. A la fecha, el Gobierno de Colombia se encuentra adelantando el proceso de implementación de los acuerdos e iniciando nuevas conversaciones con el ELN, que ha manifestado la intención de contribuir al final del conflicto.37​

Colombia tiene una economía diversificada y posee un importante componente de servicios. La producción económica del país está dominada por su demanda interna y el gasto en consumo de los hogares es el mayor componente del PIB.38​ El PIB en 2016 fue de 720 151 millones de dólares.39​

El índice de desarrollo humano colombiano es de 0,767 y su esperanza de vida promedio es de 77,46 años en el año 2024.40​

Colombia es parte del grupo de los CIVETS, considerados como seis principales mercados emergentes. Es miembro de la OCDE,41​ la ONU, la OEA, la Alianza del Pacífico, la CAN y de otras organizaciones internacionales; también es el único país de Latinoamérica que es socio global de la OTAN. Es el segundo país con mayor índice de desigualdad en América Latina, después de Brasil, y empatado con Panamá, según la base de datos del Banco Mundial.42​

Es la segunda nación más biodiversa del mundo, contando con 67 000 especies registradas;43​ no obstante, un estudio lo ubica entre los ocho países responsables de la mitad de la destrucción de biodiversidad en el mundo.44​ Por otra parte, es el país de América Latina con más conflictos ecológicos entre la población local y empresas multinacionales en áreas de especial protección ambiental.45​46​ Para proteger su medio ambiente el país cuenta con instrumentos como la Política Nacional de Cambio Climático y el impuesto al carbono.47​

La producción de electricidad en Colombia proviene principalmente de fuentes de energía renovables. 70% se obtiene de la generación hidroeléctrica.48​
"""
texto = texto.capitalize()
letras = {}
for letra in texto:
    if not letra in letras:
        letras[letra] = 0
    letras[letra] = letras[letra] + 1

print(letras)
