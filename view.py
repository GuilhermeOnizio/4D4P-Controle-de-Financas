from models import Conta, engine
from sqlmodel import Session, select

def criar_conta(conta: Conta):
    with Session(engine) as session:
        session.add(conta)
        session.commit()

conta = Conta(valor=10, banco='Nubank')
criar_conta(conta)