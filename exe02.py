#substituindo caracteres repetidos
name = "fifa"
cha = name[0].lower()
new_name = name.replace(cha,'$')
new_name = cha + new_name[1:]
print(new_name)


#troca de caracteres
st1 = 'cab'
st2 = 'zyx'
new_st1 = st2[:2]
new_st2 = st1[:2]
print(new_st1 +  st1[2:])
print(new_st2 +  st2[2:])