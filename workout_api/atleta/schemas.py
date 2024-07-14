from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from workout_api.contrib.models import Base, BaseModel
from sqlalchemy.exc import IntegrityError

class AtletaModel(BaseModel):
    __tablename__ = 'atletas'

    pk_id: Column[int] = Column(Integer, primary_key=True)
    nome: Column[str] = Column(String(50), nullable=False)
    cpf: Column[str] = Column(String(11), unique=True, nullable=False)
    idade: Column[int] = Column(Integer, nullable=False)
    peso: Column[float] = Column(Float, nullable=False)
    altura: Column[float] = Column(Float, nullable=False)
    sexo: Column[str] = Column(String(1), nullable=False)
    created_at: Column[datetime] = Column(DateTime, nullable=False, default=datetime.utcnow)
    categoria: relationship = relationship("CategoriaModel", back_populates="atleta", lazy='selectin')
    categoria_id: Column[int] = Column(ForeignKey("categorias.pk_id"))
    centro_treinamento: relationship = relationship("CentroTreinamentoModel", back_populates="atleta", lazy='selectin')
    centro_treinamento_id: Column[int] = Column(ForeignKey("centros_treinamento.pk_id"))
