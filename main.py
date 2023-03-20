from typing import Union
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from pathlib import Path
import pandas as pd

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def read_excel(request: Request):
    # read the Excel file using pandas
    df = pd.read_excel("./uploads/input.xlsx")

    # convert the DataFrame to an HTML table
    html_table = df.to_html()

    # render the HTML table using a Jinja2 template
    return templates.TemplateResponse("table.html", {"request": request, "table": html_table})


@app.get("/orders")
def read_item():
    return [
        [
            {
                "itemNo": "111500-36",
                "description": "#3 P/1 DOT   CANOE WOBBLER",
                "totalQty": 6,
                "customerName": "Bass Pro Inc. (Canada)",
                "customerQty": 6,
                "requestedShipDate": "22-Nov-22"
            },
            {
                "itemNo": "100661-37",
                "description": "#1 PACK TROUT 6/PACK",
                "totalQty": 2,
                "customerName": "C.S.I. Sporting Goods Cnd Inc",
                "customerQty": 2,
                "requestedShipDate": "22-Nov-22"
            },
            {
                "itemNo": "100662-37",
                "description": "#2 PACK TROUT 6/PACK",
                "totalQty": 10,
                "customerName": "Canadian Tire Corporation",
                "customerQty": 7,
                "requestedShipDate": "22-Nov-22"
            },
            {
                "itemNo": "",
                "description": "",
                "totalQty": "",
                "customerName": "QUEBEC FISHING TACKLE 9294-7183 QUE INC",
                "customerQty": 3,
                "requestedShipDate": "22-Nov-22"
            },
            {
                "itemNo": "100663-37",
                "description": "#3 PACK BASS 'N WALLEYE",
                "totalQty": 5,
                "customerName": "QUEBEC FISHING TACKLE 9294-7183 QUE INC",
                "customerQty": 5,
                "requestedShipDate": "22-Nov-22"
            },
            {
                "itemNo": "100664-37",
                "description": "#4 PACK ICE FISHING 6/PK",
                "totalQty": 6,
                "customerName": "Bass Pro Inc. (Canada)",
                "customerQty": 3,
                "requestedShipDate": "22-Nov-22"
            },
            {
                "itemNo": "",
                "description": "",
                "totalQty": "",
                "customerName": "QUEBEC FISHING TACKLE 9294-7183 QUE INC",
                "customerQty": 3,
                "requestedShipDate": "24-Nov-22"
            },
            {
                "itemNo": "100665-37",
                "description": "#5 PACK TROUT 'N BASS 6/PK",
                "totalQty": 20,
                "customerName": "Bass Pro Inc. (Canada)",
                "customerQty": 5,
                "requestedShipDate": "26-Nov-22"
            },
            {
                "itemNo": "",
                "description": "",
                "totalQty": "",
                "customerName": "C.S.I. Sporting Goods Cnd Inc",
                "customerQty": 5,
                "requestedShipDate": "27-Nov-22"
            },
            {
                "itemNo": "",
                "description": "",
                "totalQty": "",
                "customerName": "QUEBEC FISHING TACKLE 9294-7183 QUE INC",
                "customerQty": 5,
                "requestedShipDate": "28-Nov-22"
            },
            {
                "itemNo": "",
                "description": "",
                "totalQty": "",
                "customerName": "Bass Pro Inc. (Canada)",
                "customerQty": 5,
                "requestedShipDate": "29-Nov-22"
            },
            {
                "itemNo": "171275-46",
                "description": "2 3/4       RAINBOW LURE",
                "totalQty": 24,
                "customerName": "C.S.I. Sporting Goods Cnd Inc",
                "customerQty": 24,
                "requestedShipDate": "01-Dec-22"
            },
            {
                "itemNo": "100109-37",
                "description": "#109 ASSORTMENT",
                "totalQty": 6,
                "customerName": "Bass Pro Inc. (Canada)",
                "customerQty": 6,
                "requestedShipDate": "03-Dec-22"
            },
            {
                "itemNo": "100400-08",
                "description": "LIVE SPOON (SS) YLW PERCH  4 PACK",
                "totalQty": 120,
                "customerName": "Canadian Tire Corporation",
                "customerQty": 120,
                "requestedShipDate": "03-Dec-22"
            }
        ]
    ]


@app.post("/upload-orders")
async def upload_orders(file: UploadFile = File(...)):
    file_location = Path("./uploads") / file.filename
    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())
    return {"filename": file.filename}
