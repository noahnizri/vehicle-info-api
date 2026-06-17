from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import re


app = FastAPI(
    title="Insurance Company Stub API",
    description="API for retrieving vehicle information by license plate",
    version="1.0.0",
)


class VehicleRequest(BaseModel):
    license_plate: str = Field(
        ...,
        description="מספר רכב (7 או 8 ספרות)",
        examples=["12345678"],
    )


class VehicleData(BaseModel):
    license_plate: str = Field(..., description="מספר רכב")
    manufacturer: str = Field(..., description="יצרן הרכב")
    model: str = Field(..., description="דגם הרכב")
    year: int = Field(..., description="שנת ייצור")
    color: str = Field(..., description="צבע הרכב")


class SuccessResponse(BaseModel):
    success: bool = Field(default=True, description="האם הבקשה הצליחה")
    data: VehicleData = Field(..., description="פרטי הרכב")


class ErrorResponse(BaseModel):
    success: bool = Field(default=False, description="האם הבקשה הצליחה")
    error: str = Field(..., description="הודעת שגיאה")


MOCK_VEHICLES_DB = {
    "00000000": {
    "license_plate": "00000000",
    "manufacturer": "הונדה",
    "model": "סיוויק",
    "year": 2017,
    "color": "לבן",
    },
    "11111111": {
        "license_plate": "11111111",
        "manufacturer": "טויוטה",
        "model": "קורולה",
        "year": 2020,
        "color": "לבן",
    },
    "22222222": {
        "license_plate": "22222222",
        "manufacturer": "יונדאי",
        "model": "איוניק",
        "year": 2022,
        "color": "אפור",
    },
    "33333333": {
        "license_plate": "33333333",
        "manufacturer": "קיה",
        "model": "פיקנטו",
        "year": 2021,
        "color": "שחור",
    },
    "44444444": {
        "license_plate": "44444444",
        "manufacturer": "מאזדה",
        "model": "3",
        "year": 2019,
        "color": "כחול",
    },
    "55555555": {
        "license_plate": "55555555",
        "manufacturer": "סקודה",
        "model": "אוקטביה",
        "year": 2023,
        "color": "כסוף",
    },
    "66666666": {
        "license_plate": "66666666",
        "manufacturer": "סוזוקי",
        "model": "סוויפט",
        "year": 2018,
        "color": "אדום",
    },
    "77777777": {
        "license_plate": "77777777",
        "manufacturer": "מיצובישי",
        "model": "אאוטלנדר",
        "year": 2022,
        "color": "שחור",
    },
    "88888888": {
        "license_plate": "88888888",
        "manufacturer": "רנו",
        "model": "קליאו",
        "year": 2021,
        "color": "לבן",
    },
    "99999999": {
        "license_plate": "99999999",
        "manufacturer": "הונדה",
        "model": "סיוויק",
        "year": 2017,
        "color": "לבן",
    },

}


def normalize_license_plate(license_plate: str) -> str:
    return license_plate.replace("-", "").replace(" ", "").strip()


def is_valid_license_plate(license_plate: str) -> bool:
    return bool(re.fullmatch(r"\d{7,8}", license_plate))


@app.get("/", tags=["Health"])
def root():
    """Health check endpoint"""
    return "Insurance Company Stub API is running"


@app.get("/health", tags=["Health"])
def health_check():
    """Health check for Cloud Run"""
    return "ok"


@app.post(
    "/vehicle-info",
    response_model=SuccessResponse,
    responses={
        400: {
            "model": ErrorResponse,
            "description": "פורמט מספר רכב לא תקין",
        },
        404: {
            "model": ErrorResponse,
            "description": "רכב לא נמצא במאגר",
        },
    },
    tags=["Vehicle Information"],
    summary="קבלת פרטי רכב לפי מספר רכב",
    description="מחזיר יצרן, דגם, שנה וצבע לפי מספר רכב (7 או 8 ספרות)",
)
def get_vehicle_info(request: VehicleRequest):
    license_plate = normalize_license_plate(request.license_plate)

    if not is_valid_license_plate(license_plate):
        raise HTTPException(
            status_code=400,
            detail={
                "success": False,
                "error": "פורמט מספר רכב לא תקין. יש להזין 7 או 8 ספרות.",
            },
        )

    vehicle = MOCK_VEHICLES_DB.get(license_plate)

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail={
                "success": False,
                "error": "רכב לא נמצא במאגר.",
            },
        )

    return {
        "success": True,
        "data": vehicle,
    }