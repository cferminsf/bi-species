USE [UnoSof]
GO

/****** Object:  Table [Facturas]    Script Date: 30/05/2023 14:27:30 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [T_Species](
	[gu_option] [nvarchar](max) NULL,
	[nm_option] [nvarchar](max) NULL,
	[od_option] [int] NULL,
	[tx_code_1] [nvarchar](max) NULL,
	[id_venture] [nvarchar](max) NULL,
	[tx_code_commercial] [nvarchar](max) NULL,
	[tx_code_hts] [nvarchar](max) NULL
)
GO
