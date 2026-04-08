from typing import Any, Self

from pydantic_core import MultiHostUrl


class CeleryDsn:
    def __init__(self, url: MultiHostUrl) -> None:
        self._url = url

    def __str__(self) -> str:
        """The URL as a string, this will punycode encode the host if required."""
        return str(self._url)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({str(self._url)!r})"

    def __deepcopy__(self, _: dict) -> Self:
        return self.__class__(self._url)

    def __eq__(self, other: Any) -> bool:
        return self.__class__ is other.__class__ and self._url == other._url

    def __hash__(self) -> int:
        return hash(self._url)

    def __len__(self) -> int:
        return len(str(self._url))

    @classmethod
    def build(
        cls, host: str, port: int, username: str, password: str, vhost: str
    ) -> Self:
        return cls(
            MultiHostUrl.build(
                scheme="amqp",
                host=host,
                port=port,
                username=username,
                password=password,
                path=vhost,
            )
        )
