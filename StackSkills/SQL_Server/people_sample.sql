/****** Script for SelectTopNRows command from SSMS  ******/
SELECT TOP (1000) [Title]
      ,[FirstName]
      ,[MiddleName]
      ,[LastName]
      ,[Suffix]
      ,[ModifiedDate]
  FROM [Sample_DB].[dbo].[people$]