// _pdvpycam24.h : main header file for the _pdvpycam24 DLL
//

#pragma once

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// main symbols


// Cpdvpycam24App
// See _pdvpycam24.cpp for the implementation of this class
//

class Cpdvpycam24App : public CWinApp
{
public:
	Cpdvpycam24App();

// Overrides
public:
	virtual BOOL InitInstance();

	DECLARE_MESSAGE_MAP()
};
