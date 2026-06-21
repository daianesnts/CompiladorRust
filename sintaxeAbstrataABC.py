from abc import abstractmethod
from abc import ABC

class Program(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class TopDecl(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class FuncDecl(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Signature(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class SignatureI(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class SignatureP(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class SignatureNP(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class SigParams(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class SigParam(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Body(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class StructDecl(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class StructFields(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class StructField(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class TraitDecl(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class TraitBody(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class TraitSignatures(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class TraitMethod(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class TraitSignature(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class TraitSignatureP(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass 

class Stmts(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Stm(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Ifr(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Decl(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class TypeDecl(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Exp(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpAssign(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpOr(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpAnd(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpRel(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpBitOr(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpBitXor(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpBitAnd(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpShift(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpAdd(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpMul(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpUnary(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class ExpPrimary(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Call(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Args(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass