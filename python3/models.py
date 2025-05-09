# DISCLAIMER:
# This sample code is provided for illustrative purposes only.
# It is not intended for production use and comes with no warranties.

from pydantic import BaseModel, RootModel
from typing import List, Optional, Union

class Fixture(BaseModel):
    date: str
    fixtureType: str
    fixtureString: str
    voyageType: Optional[str] = None
    shipName: Optional[str] = None
    relet: Optional[str] = None
    period: Optional[str] = None
    buildYear: Optional[str] = None
    dwt: Optional[float] = None
    cargoSizeType: Optional[str] = None
    cargoSubType: Optional[str] = None
    cargoSizeUpper: Optional[float] = None
    cargoSizeLower: Optional[float] = None
    margin: Optional[str] = None
    deliveryArea: Optional[str] = None
    deliveryPort: Optional[str] = None
    laycanType: Optional[str] = None
    rangeStart: Optional[str] = None
    rangeEnd: Optional[str] = None
    freeText: Optional[str] = None
    loadArea: Optional[str] = None
    loadPort: Optional[str] = None
    disachargePort: Optional[str] = None
    rateAndTerms: Optional[str] = None
    charterer: Optional[str] = None
    comment: Optional[str] = None
    bold: Optional[bool] = None
    tripDescriptionPeriodInfo: Optional[str] = None
    viaPortReletRateBallastBonus: Optional[str] = None
    speedAndConsumption: Optional[str] = None


class FixtureDataSet(BaseModel):
    fixturesFrom: str
    fixturesTo: str
    fixtures: List[Fixture]
    id: Optional[str] = None
    name: str
    apiIdentifier: str


class Datum(BaseModel):
    value: float
    date: str


class IndexDataSet(BaseModel):
    id: str
    shortCode: str
    shortDescription: Optional[str]
    displayGroup: str
    datumUnit: Optional[str]
    datumPrecision: int
    breeoiEco: Optional[float]
    breeoiFull: Optional[float]
    data: List[Datum]
    apiIdentifier: str


class Projection(BaseModel):
    identifier: str
    period: str
    value: float
    validFrom: Optional[str]
    validTo: Optional[str]
    nextRolloverDate: Optional[str]
    archiveDate: str


class Group(BaseModel):
    periodType: str
    projections: List[Projection]


class Grouping(BaseModel):
    date: str
    groups: List[Group]


class GroupedIndexDataSet(BaseModel):
    id: str
    shortCode: str
    datumUnit: Optional[str]
    datumPrecision: int
    groupings: List[Grouping]
    apiIdentifier: str
    shortDescription: Optional[str]
    dataSet: Optional[IndexDataSet]


class GroupedTrade(BaseModel):
    provider: str
    quantity: float
    year: int
    month: int
    clearedOnDate: str
    tradedDate: str
    premium: Optional[float]
    optionsType: Optional[str]
    strikePrice: float


class TimePeriodTrade(BaseModel):
    period: str
    averagePrice: float
    aggregateLots: float


class TimePeriod(BaseModel):
    key: str
    trades: List[TimePeriodTrade]


class IntradayTrade(BaseModel):
    tradedOn: str
    timePeriods: List[TimePeriod]


class TradeDataSet(BaseModel):
    id: str
    name: str
    category: str
    sector: str
    vessel: str
    shortDescription: Optional[str]
    tradedFrom: Optional[str]
    tradedTo: Optional[str]
    shortCode: str
    groupedTrades: Optional[List[GroupedTrade]]
    intradayTrades: Optional[List[IntradayTrade]]
    apiIdentifier: str


FeedItem = Union[FixtureDataSet, IndexDataSet, GroupedIndexDataSet, TradeDataSet]


class FeedResponse(RootModel[List[FeedItem]]):
    pass
