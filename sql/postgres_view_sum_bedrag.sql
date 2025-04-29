/*
SELECT SUM(bedrag) AS total_bedrag
FROM public.afschrijvingen;
*/
SELECT *
FROM (
    SELECT 
        afschrijving, beschrijving, datum, rekening, bedrag, 1 AS sort_order
    FROM public.afschrijvingen

    UNION ALL

    SELECT 
        'AFSCHRIJVINGEN' AS afschrijving,
        'TOTAAL' AS beschrijving,
        NULL AS datum,
        'REKENINGEN' AS rekening,
        SUM(bedrag) AS bedrag,
        0 AS sort_order
    FROM public.afschrijvingen
) AS combined
ORDER BY sort_order, bedrag DESC, datum;

/*
SELECT id, afschrijving, beschrijving, bedrag, datum, rekening
FROM public.afschrijvingen

UNION ALL

SELECT 
    NULL AS id, 
    NULL AS afschrijving, 
    'TOTAAL' AS beschrijving, 
    SUM(bedrag) AS bedrag, 
    NULL AS datum, 
    NULL AS rekening
FROM public.afschrijvingen;
*/

-- Sum for specific date!
SELECT *
FROM (
    SELECT 
        id, afschrijving, beschrijving, bedrag, datum, rekening, 1 AS sort_order
    FROM public.afschrijvingen
    WHERE datum = '1e'

    UNION ALL

    SELECT 
        NULL AS id,
        NULL AS afschrijving,
        'TOTAAL' AS beschrijving,
        SUM(bedrag) AS bedrag,
        NULL AS datum,
        NULL AS rekening,
        0 AS sort_order
    FROM public.afschrijvingen
    WHERE datum = '1e'
) AS combined
ORDER BY sort_order, bedrag DESC, datum;