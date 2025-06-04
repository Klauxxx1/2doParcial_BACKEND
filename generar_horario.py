import argparse
from collections import defaultdict

data = [
    {
        "id": 1671,
        "dia": "jueves",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 284,
        "materia": 707,
        "profesor": 632
    },
    {
        "id": 1672,
        "dia": "jueves",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 284,
        "materia": 708,
        "profesor": 634
    },
    {
        "id": 1673,
        "dia": "viernes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 284,
        "materia": 709,
        "profesor": 638
    },
    {
        "id": 1674,
        "dia": "viernes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 284,
        "materia": 710,
        "profesor": 640
    },
    {
        "id": 1675,
        "dia": "lunes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 285,
        "materia": 701,
        "profesor": 631
    },
    {
        "id": 1676,
        "dia": "lunes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 285,
        "materia": 702,
        "profesor": 633
    },
    {
        "id": 1677,
        "dia": "martes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 285,
        "materia": 703,
        "profesor": 637
    },
    {
        "id": 1678,
        "dia": "martes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 285,
        "materia": 704,
        "profesor": 636
    },
    {
        "id": 1679,
        "dia": "miércoles",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 285,
        "materia": 705,
        "profesor": 635
    },
    {
        "id": 1680,
        "dia": "miércoles",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 285,
        "materia": 706,
        "profesor": 630
    },
    {
        "id": 1681,
        "dia": "jueves",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 285,
        "materia": 707,
        "profesor": 641
    },
    {
        "id": 1682,
        "dia": "jueves",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 285,
        "materia": 708,
        "profesor": 639
    },
    {
        "id": 1683,
        "dia": "viernes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 285,
        "materia": 709,
        "profesor": 634
    },
    {
        "id": 1684,
        "dia": "viernes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 285,
        "materia": 710,
        "profesor": 632
    },
    {
        "id": 1685,
        "dia": "lunes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 286,
        "materia": 701,
        "profesor": 640
    },
    {
        "id": 1686,
        "dia": "lunes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 286,
        "materia": 702,
        "profesor": 638
    },
    {
        "id": 1687,
        "dia": "martes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 286,
        "materia": 703,
        "profesor": 631
    },
    {
        "id": 1688,
        "dia": "martes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 286,
        "materia": 704,
        "profesor": 633
    },
    {
        "id": 1689,
        "dia": "miércoles",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 286,
        "materia": 705,
        "profesor": 637
    },
    {
        "id": 1690,
        "dia": "miércoles",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 286,
        "materia": 706,
        "profesor": 636
    },
    {
        "id": 1691,
        "dia": "jueves",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 286,
        "materia": 707,
        "profesor": 635
    },
    {
        "id": 1692,
        "dia": "jueves",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 286,
        "materia": 708,
        "profesor": 630
    },
    {
        "id": 1693,
        "dia": "viernes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 286,
        "materia": 709,
        "profesor": 641
    },
    {
        "id": 1694,
        "dia": "viernes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 286,
        "materia": 710,
        "profesor": 639
    },
    {
        "id": 1695,
        "dia": "lunes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 287,
        "materia": 701,
        "profesor": 634
    },
    {
        "id": 1696,
        "dia": "lunes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 287,
        "materia": 702,
        "profesor": 632
    },
    {
        "id": 1697,
        "dia": "martes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 287,
        "materia": 703,
        "profesor": 640
    },
    {
        "id": 1698,
        "dia": "martes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 287,
        "materia": 704,
        "profesor": 638
    },
    {
        "id": 1699,
        "dia": "miércoles",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 287,
        "materia": 705,
        "profesor": 631
    },
    {
        "id": 1700,
        "dia": "miércoles",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 287,
        "materia": 706,
        "profesor": 633
    },
    {
        "id": 1701,
        "dia": "jueves",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 287,
        "materia": 707,
        "profesor": 637
    },
    {
        "id": 1702,
        "dia": "jueves",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 287,
        "materia": 708,
        "profesor": 636
    },
    {
        "id": 1703,
        "dia": "viernes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 287,
        "materia": 709,
        "profesor": 635
    },
    {
        "id": 1704,
        "dia": "viernes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 287,
        "materia": 710,
        "profesor": 630
    },
    {
        "id": 1705,
        "dia": "lunes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 288,
        "materia": 701,
        "profesor": 641
    },
    {
        "id": 1706,
        "dia": "lunes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 288,
        "materia": 702,
        "profesor": 639
    },
    {
        "id": 1707,
        "dia": "martes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 288,
        "materia": 703,
        "profesor": 634
    },
    {
        "id": 1708,
        "dia": "martes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 288,
        "materia": 704,
        "profesor": 632
    },
    {
        "id": 1709,
        "dia": "miércoles",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 288,
        "materia": 705,
        "profesor": 640
    },
    {
        "id": 1710,
        "dia": "miércoles",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 288,
        "materia": 706,
        "profesor": 638
    },
    {
        "id": 1711,
        "dia": "jueves",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 288,
        "materia": 707,
        "profesor": 631
    },
    {
        "id": 1712,
        "dia": "jueves",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 288,
        "materia": 708,
        "profesor": 633
    },
    {
        "id": 1713,
        "dia": "viernes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 288,
        "materia": 709,
        "profesor": 637
    },
    {
        "id": 1714,
        "dia": "viernes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 288,
        "materia": 710,
        "profesor": 636
    },
    {
        "id": 1715,
        "dia": "lunes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 289,
        "materia": 701,
        "profesor": 635
    },
    {
        "id": 1716,
        "dia": "lunes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 289,
        "materia": 702,
        "profesor": 630
    },
    {
        "id": 1717,
        "dia": "martes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 289,
        "materia": 703,
        "profesor": 641
    },
    {
        "id": 1718,
        "dia": "martes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 289,
        "materia": 704,
        "profesor": 639
    },
    {
        "id": 1719,
        "dia": "miércoles",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 289,
        "materia": 705,
        "profesor": 634
    },
    {
        "id": 1720,
        "dia": "miércoles",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 289,
        "materia": 706,
        "profesor": 632
    },
    {
        "id": 1721,
        "dia": "jueves",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 289,
        "materia": 707,
        "profesor": 640
    },
    {
        "id": 1722,
        "dia": "jueves",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 289,
        "materia": 708,
        "profesor": 638
    },
    {
        "id": 1723,
        "dia": "viernes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 289,
        "materia": 709,
        "profesor": 631
    },
    {
        "id": 1724,
        "dia": "viernes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 289,
        "materia": 710,
        "profesor": 633
    },
    {
        "id": 1725,
        "dia": "lunes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 290,
        "materia": 701,
        "profesor": 637
    },
    {
        "id": 1726,
        "dia": "lunes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 290,
        "materia": 702,
        "profesor": 636
    },
    {
        "id": 1615,
        "dia": "lunes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 279,
        "materia": 701,
        "profesor": 633
    },
    {
        "id": 1616,
        "dia": "lunes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 279,
        "materia": 702,
        "profesor": 631
    },
    {
        "id": 1617,
        "dia": "martes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 279,
        "materia": 703,
        "profesor": 636
    },
    {
        "id": 1618,
        "dia": "martes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 279,
        "materia": 704,
        "profesor": 637
    },
    {
        "id": 1619,
        "dia": "miércoles",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 279,
        "materia": 705,
        "profesor": 630
    },
    {
        "id": 1620,
        "dia": "miércoles",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 279,
        "materia": 706,
        "profesor": 635
    },
    {
        "id": 1621,
        "dia": "jueves",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 279,
        "materia": 707,
        "profesor": 639
    },
    {
        "id": 1622,
        "dia": "jueves",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 279,
        "materia": 708,
        "profesor": 641
    },
    {
        "id": 1623,
        "dia": "viernes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 279,
        "materia": 709,
        "profesor": 632
    },
    {
        "id": 1624,
        "dia": "viernes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 279,
        "materia": 710,
        "profesor": 634
    },
    {
        "id": 1625,
        "dia": "lunes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 280,
        "materia": 701,
        "profesor": 638
    },
    {
        "id": 1626,
        "dia": "lunes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 280,
        "materia": 702,
        "profesor": 640
    },
    {
        "id": 1627,
        "dia": "martes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 280,
        "materia": 703,
        "profesor": 633
    },
    {
        "id": 1628,
        "dia": "martes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 280,
        "materia": 704,
        "profesor": 631
    },
    {
        "id": 1629,
        "dia": "miércoles",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 280,
        "materia": 705,
        "profesor": 636
    },
    {
        "id": 1630,
        "dia": "miércoles",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 280,
        "materia": 706,
        "profesor": 637
    },
    {
        "id": 1631,
        "dia": "jueves",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 280,
        "materia": 707,
        "profesor": 630
    },
    {
        "id": 1632,
        "dia": "jueves",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 280,
        "materia": 708,
        "profesor": 635
    },
    {
        "id": 1633,
        "dia": "viernes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 280,
        "materia": 709,
        "profesor": 639
    },
    {
        "id": 1634,
        "dia": "viernes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 280,
        "materia": 710,
        "profesor": 641
    },
    {
        "id": 1635,
        "dia": "lunes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 281,
        "materia": 701,
        "profesor": 632
    },
    {
        "id": 1636,
        "dia": "lunes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 281,
        "materia": 702,
        "profesor": 634
    },
    {
        "id": 1637,
        "dia": "martes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 281,
        "materia": 703,
        "profesor": 638
    },
    {
        "id": 1638,
        "dia": "martes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 281,
        "materia": 704,
        "profesor": 640
    },
    {
        "id": 1639,
        "dia": "miércoles",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 281,
        "materia": 705,
        "profesor": 633
    },
    {
        "id": 1640,
        "dia": "miércoles",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 281,
        "materia": 706,
        "profesor": 631
    },
    {
        "id": 1641,
        "dia": "jueves",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 281,
        "materia": 707,
        "profesor": 636
    },
    {
        "id": 1642,
        "dia": "jueves",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 281,
        "materia": 708,
        "profesor": 637
    },
    {
        "id": 1643,
        "dia": "viernes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 281,
        "materia": 709,
        "profesor": 630
    },
    {
        "id": 1644,
        "dia": "viernes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 281,
        "materia": 710,
        "profesor": 635
    },
    {
        "id": 1645,
        "dia": "lunes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 282,
        "materia": 701,
        "profesor": 639
    },
    {
        "id": 1646,
        "dia": "lunes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 282,
        "materia": 702,
        "profesor": 641
    },
    {
        "id": 1647,
        "dia": "martes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 282,
        "materia": 703,
        "profesor": 632
    },
    {
        "id": 1648,
        "dia": "martes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 282,
        "materia": 704,
        "profesor": 634
    },
    {
        "id": 1649,
        "dia": "miércoles",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 282,
        "materia": 705,
        "profesor": 638
    },
    {
        "id": 1650,
        "dia": "miércoles",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 282,
        "materia": 706,
        "profesor": 640
    },
    {
        "id": 1651,
        "dia": "jueves",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 282,
        "materia": 707,
        "profesor": 633
    },
    {
        "id": 1652,
        "dia": "jueves",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 282,
        "materia": 708,
        "profesor": 631
    },
    {
        "id": 1653,
        "dia": "viernes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 282,
        "materia": 709,
        "profesor": 636
    },
    {
        "id": 1654,
        "dia": "viernes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 282,
        "materia": 710,
        "profesor": 637
    },
    {
        "id": 1655,
        "dia": "lunes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 283,
        "materia": 701,
        "profesor": 630
    },
    {
        "id": 1656,
        "dia": "lunes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 283,
        "materia": 702,
        "profesor": 635
    },
    {
        "id": 1657,
        "dia": "martes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 283,
        "materia": 703,
        "profesor": 639
    },
    {
        "id": 1658,
        "dia": "martes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 283,
        "materia": 704,
        "profesor": 641
    },
    {
        "id": 1659,
        "dia": "miércoles",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 283,
        "materia": 705,
        "profesor": 632
    },
    {
        "id": 1660,
        "dia": "miércoles",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 283,
        "materia": 706,
        "profesor": 634
    },
    {
        "id": 1661,
        "dia": "jueves",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 283,
        "materia": 707,
        "profesor": 638
    },
    {
        "id": 1662,
        "dia": "jueves",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 283,
        "materia": 708,
        "profesor": 640
    },
    {
        "id": 1663,
        "dia": "viernes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 283,
        "materia": 709,
        "profesor": 633
    },
    {
        "id": 1664,
        "dia": "viernes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 283,
        "materia": 710,
        "profesor": 631
    },
    {
        "id": 1665,
        "dia": "lunes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 284,
        "materia": 701,
        "profesor": 636
    },
    {
        "id": 1666,
        "dia": "lunes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 284,
        "materia": 702,
        "profesor": 637
    },
    {
        "id": 1667,
        "dia": "martes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 284,
        "materia": 703,
        "profesor": 630
    },
    {
        "id": 1668,
        "dia": "martes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 284,
        "materia": 704,
        "profesor": 635
    },
    {
        "id": 1669,
        "dia": "miércoles",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 284,
        "materia": 705,
        "profesor": 639
    },
    {
        "id": 1670,
        "dia": "miércoles",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 284,
        "materia": 706,
        "profesor": 641
    },
    {
        "id": 1727,
        "dia": "martes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 290,
        "materia": 703,
        "profesor": 635
    },
    {
        "id": 1728,
        "dia": "martes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 290,
        "materia": 704,
        "profesor": 630
    },
    {
        "id": 1729,
        "dia": "miércoles",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 290,
        "materia": 705,
        "profesor": 641
    },
    {
        "id": 1730,
        "dia": "miércoles",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 290,
        "materia": 706,
        "profesor": 639
    },
    {
        "id": 1731,
        "dia": "jueves",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 290,
        "materia": 707,
        "profesor": 634
    },
    {
        "id": 1732,
        "dia": "jueves",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 290,
        "materia": 708,
        "profesor": 632
    },
    {
        "id": 1733,
        "dia": "viernes",
        "bloque_1_inicio": "07:30:00",
        "bloque_1_fin": "09:30:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 290,
        "materia": 709,
        "profesor": 640
    },
    {
        "id": 1734,
        "dia": "viernes",
        "bloque_1_inicio": "10:00:00",
        "bloque_1_fin": "12:00:00",
        "bloque_2_inicio": "00:00:00",
        "bloque_2_fin": "00:00:00",
        "curso": 290,
        "materia": 710,
        "profesor": 638
    }
]

def generar_tabla_html(data, id_curso):
    dias = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes']
    bloques = ["07:30-09:30", "10:00-12:00"]

    tabla = {bloque: {dia: "" for dia in dias} for bloque in bloques}

    for clase in data:
        if clase["curso"] != id_curso:
            continue

        dia = clase["dia"]
        if dia not in dias:
            continue

        if clase["bloque_1_inicio"] != "00:00:00":
            hora = f"{clase['bloque_1_inicio'][:5]}-{clase['bloque_1_fin'][:5]}"
            info = f"Materia {clase['materia']}<br>Prof. {clase['profesor']}"
            tabla[hora][dia] = info

        if clase["bloque_2_inicio"] != "00:00:00":
            hora = f"{clase['bloque_2_inicio'][:5]}-{clase['bloque_2_fin'][:5]}"
            info = f"Materia {clase['materia']}<br>Prof. {clase['profesor']}"
            tabla[hora][dia] = info

    # Ordenar bloques de forma cronológica
    bloques_ordenados = sorted(tabla.keys())

    html = "<html><head><style>"
    html += "table {border-collapse: collapse; width: 100%;}"
    html += "th, td {border: 1px solid black; padding: 8px; text-align: center;}"
    html += "th {background-color: #f2f2f2;}"
    html += "</style></head><body>"
    html += f"<h2>Horario Curso {id_curso}</h2><table>"
    html += "<tr><th>Hora</th>" + "".join(f"<th>{d.capitalize()}</th>" for d in dias) + "</tr>"

    for bloque in bloques_ordenados:
        html += f"<tr><td><b>{bloque}</b></td>"
        for dia in dias:
            html += f"<td>{tabla[bloque][dia]}</td>"
        html += "</tr>"

    html += "</table></body></html>"

    with open("horario_curso.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("✅ Archivo horario_curso.html generado correctamente.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generar horario HTML por curso")
    parser.add_argument("id_curso", type=int, help="ID del curso")
    args = parser.parse_args()
    generar_tabla_html(data, args.id_curso)
