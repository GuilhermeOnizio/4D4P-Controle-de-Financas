from models import Conta, engine, Bancos
from sqlmodel import Session, select

def criar_conta(conta: Conta):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.banco == conta.banco)
        results = session.exec(statement).all()
        
        if results:
            print('Já existe uma conta com esse banco')
            return

        session.add(conta)
        session.commit()
        return conta

conta = Conta(valor=10, banco=Bancos.INTER)
criar_conta(conta)