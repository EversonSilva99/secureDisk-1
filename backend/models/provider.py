from models import db


class ProviderModel(db.Model):
    __tablename__ = 'provider'

    id: int = db.Column(db.Integer, primary_key=True)
    business_name: str = db.Column(db.String(30), nullable=False)
    fantasy_name: str = db.Column(db.String(100), nullable=False)
    cnpj: str = db.Column(db.String(14), nullable=False, unique=True)
    tel: str = db.Column(db.String(10), nullable=False)
    cel: str = db.Column(db.String(11), nullable=True)
    email: str = db.Column(db.String(128), nullable=False, unique=True)
    password: str = db.Column(db.String(256), nullable=True)
    status: str = db.Column(db.String(100), nullable=False, default='ativo')
    created_date = db.Column(db.Date)
    

    @staticmethod
    def get_by_email(email):
        return db.session.query(ProviderModel).filter_by(email=email).first()

    @staticmethod
    def get_by_id(id_user: int):
        return ProviderModel.query.filter_by(id=id_user).first()
    @staticmethod
    def get_cpf(cnpj):
        return ProviderModel.query.get(cnpj=cnpj)
    
    @staticmethod
    def get_status(status):
        return InsuredModel.query.filter_by(status=status).all()

    @staticmethod
    def get_by_ids(ids_user):
        return ProviderModel.query(ProviderModel.id.in_(ids_user)).all()

    @staticmethod
    def list_all():
        return ProviderModel.query.order_by(ProviderModel.fantasy_name).all()

    @staticmethod
    def authenticate(email, password):
        user = ProviderModel.query.filter_by(email=email).first()
        if user and user.status == 'ativo':
            if password == user.password:
                return user
        return None

    def save(self):
        db.session.merge(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()