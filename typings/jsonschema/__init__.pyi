from collections.abc import Callable, Mapping

from jsonschema.protocols import Validator

class TypeChecker:
    def redefine_many(self, definitions: Mapping[str, Callable[[TypeChecker, object], bool]] = ...) -> TypeChecker: ...

class FormatChecker: ...

Draft202012Validator: type[Validator]
