// _pdvpycam23.h : main header file for the _pdvpycam23 DLL
//

#pragma once

#ifndef __AFXWIN_H__
	#error include 'stdafx.h' before including this file for PCH
#endif

#include "resource.h"		// main symbols


// Cpdvpycam23App
// See _pdvpycam23.cpp for the implementation of this class
//

class Cpdvpycam23App : public CWinApp
{
public:
	Cpdvpycam23App();

// Overrides
public:
	virtual BOOL InitInstance();

	DECLARE_MESSAGE_MAP()
};
