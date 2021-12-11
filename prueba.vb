Public Class Form1
        Dim Imc As Double
        Dim mnsj As String
        If Imc >= 18.5 And Imc <= 24.9 Then
            mnsj = "Promedio"
        ElseIf Imc >= 25 And Imc <= 29.9 Then
            mnsj = "Aumentado"
        ElseIf Imc >= 30 And Imc <= 34.9 Then
            mnsj = "Moderado"
        ElseIf Imc >= 35 And Imc <= 39.9 Then
            mnsj = "Severo"
        ElseIf Imc >= 40 Then
            mnsj = "Muy Severo"
        End If
End Class