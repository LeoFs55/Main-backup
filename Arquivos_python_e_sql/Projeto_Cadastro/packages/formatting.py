import packages.password_validation as password_validation
import packages.name_validation as name_validation
import packages.age_validation as age_validation
import packages.cpf_validation as cpf_validation
import packages.email_validation as email_validation
from copy import deepcopy
from datetime import date

def all_valid(name,surname,birth,cpf,password,email):
    nome=name_validation.name(name)
    sobrenome=name_validation.surname(surname)
    data_nascimento=age_validation.date_validation(birth)
    cpf_=cpf_validation.cpf(cpf)
    senha=password_validation.password(password)
    email_ = email_validation.email_valid(email)
    return True if nome and sobrenome and data_nascimento and cpf_ and senha and email_ else False

def data_recb(name,surname,birth,cpf,password,email):
    if all_valid(name,surname,birth,cpf,password,email):
        nome=name.lower()
        sobrenome=name.lower()
        data_nascimento=age_validation.tupla_date(birth)
        cpf_= cpf
        senha= password
        email_ = email
    return nome,sobrenome,data_nascimento,cpf_,senha,email_
