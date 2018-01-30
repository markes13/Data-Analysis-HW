Option Explicit

Sub tickers()
    Dim header_row As Integer
    
    Dim volume As Double
    volume = 0
    
    Dim ticker As String
    Dim ws As Worksheet
    Dim closing_price, opening_price As Double
    Dim last_row As Long
    Dim final_row As Long
    Dim year_change As Double
    Dim perchange As Double
    Dim l, k, x, z, u, y, i, j, b As Double
    Dim greatest_increase, greatest_decrease, total_volume As Double
    Dim open1, close1, change As Double
    Dim incstock, decstock, greatest As String
    
    For Each ws In ActiveWorkbook.Worksheets
        ws.Activate
        header_row = 2
        Range("I1").Value = "Ticker"
        Range("J1").Value = "Total Stock Volume"
        Range("K1").Value = "Opening Price"
        Range("L1").Value = "Closing Price"
        Range("M1").Value = "Year Change"
        Range("N1").Value = "% Year Change"
        last_row = Range("A999999").End(xlUp).Row
        For i = 2 To last_row
            If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
                ticker = Cells(i, 1).Value
                volume = volume + Cells(i, 7).Value
                closing_price = Cells(i, 6).Value
                Cells(header_row, 9).Value = ticker
                Cells(header_row, 10).Value = volume
                Cells(header_row, 12).Value = closing_price
                header_row = header_row + 1
                volume = 0
            ElseIf Cells(i - 1, 1).Value <> Cells(i, 1).Value Then
                opening_price = Cells(i, 3).Value
                Cells(header_row, 11).Value = opening_price
            Else
                volume = volume + Cells(i, 7).Value
            End If
        Next i
        
        For j = 2 To Range("L999999").End(xlUp).Row
            Cells(j, 13).Value = Cells(j, 12).Value - Cells(j, 11).Value
            If Cells(j, 12).Value > Cells(j, 11).Value Then
                Cells(j, 13).Interior.ColorIndex = 4
            ElseIf Cells(j, 12).Value < Cells(j, 11).Value Then
                Cells(j, 13).Interior.ColorIndex = 3
            End If
        Next j
        
        For k = 2 To Range("M65000").End(xlUp).Row
            open1 = Cells(k, 11).Value
            close1 = Cells(k, 12).Value
            If Cells(k, 11).Value = 0 Then
                Cells(k, 14).Value = "0%"
            ElseIf Cells(k, 13).Value > 0 Then
                change = close1 - open1
                perchange = (change / open1)
                Cells(k, 14).Value = perchange
            ElseIf Cells(k, 13).Value < 0 Then
                change = (open1 - close1)
                perchange = (change / open1) * -1
                Cells(k, 14).Value = perchange
            End If
        Next k
        For l = 2 To Range("M65000").End(xlUp).Row
            Cells(l, 14).NumberFormat = "0.00%"
            If Cells(l, 14).Value > 0 Then
                Cells(l, 14).Interior.ColorIndex = 4
            ElseIf Cells(l, 14).Value < 0 Then
                Cells(l, 14).Interior.ColorIndex = 3
            End If
        Next l
        For x = 2 To Range("M65000").End(xlUp).Row
            If Cells(x + 1, 14).Value > Cells(x, 14) Then
                greatest_increase = Cells(x + 1, 14).Value
            End If
        Next x
        For z = 2 To Range("M65000").End(xlUp).Row
            If Cells(z + 1, 14).Value < Cells(z, 14).Value Then
                greatest_decrease = Cells(z + 1, 14).Value
                Range("P3").Value = "Greatest % Decrease"
                Range("Q3").Value = Cells(z + 1, 1).Value
                Range("R3").Value = greatest_decrease
            End If
        Next z
        For b = 2 To Range("N65000").End(xlUp).Row
            If Cells(b + 1, 14).Value > greatest_increase Then
                greatest_increase = Cells(b + 1, 14).Value
                incstock = Cells(b + 1, 9).Value
            End If
        Next b
        For u = 2 To Range("N65000").End(xlUp).Row
           If Cells(u + 1, 14).Value < greatest_decrease Then
                greatest_decrease = Cells(u + 1, 14).Value
                decstock = Cells(u + 1, 9).Value
            End If
        Next u
        total_volume = 0
        For y = 2 To Range("N65000").End(xlUp).Row
            If Cells(y + 1, 10).Value > total_volume Then
               total_volume = Cells(y + 1, 10).Value
               greatest = Cells(y + 1, 9).Value
            End If
        Next y
        Range("Q4").Value = greatest
        Range("R4").Value = total_volume
        Range("Q1").Value = "Ticker"
        Range("R1").Value = "% Change"
        Range("P2").Value = "Greatest % Increase"
        Range("P3").Value = "Greatest % Decrease"
        Range("P4").Value = "Greatest Total Volume"
        Range("R2").Value = greatest_increase
        Range("R2").NumberFormat = "0.00%"
        Range("Q2").Value = decstock
        Range("R3").Value = greatest_decrease
        Range("R3").NumberFormat = "0.00%"
        Range("Q3").Value = incstock
        Range("Q4").Value = greatest
        Range("R4").Value = total_volume
    Next ws
End Sub
