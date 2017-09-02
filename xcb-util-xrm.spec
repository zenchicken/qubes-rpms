Name:		xcb-util-xrm
Version:	1.2
Release:	1%{?dist}
Summary:	XCB utility functions for the X resource manager

License:	Unknown
URL:		https://github.com/Airblader/xcb-util-xrm
Source0:	https://github.com/Airblader/xcb-util-xrm/releases/download/v%{version}/xcb-util-xrm-%{version}.tar.gz

BuildRequires:	xorg-x11-util-macros libxcb-devel xcb-util-devel xorg-x11-server-devel
Requires:	libxcb xcb-util xorg-x11-server-devel

Provides:	pkgconfig(xcb-xrm)

%description


%prep
%setup -q


%build
./autogen.sh --prefix="%{_prefix}" --libdir="%{_libdir}"
make %{?_smp_mflags}


%install
%make_install


%files
%doc
%{_includedir}/xcb/xcb_xrm.h
%{_libdir}/libxcb-xrm.a
%{_libdir}/libxcb-xrm.la
%{_libdir}/libxcb-xrm.so
%{_libdir}/libxcb-xrm.so.0
%{_libdir}/libxcb-xrm.so.0.0.0
%{_libdir}/pkgconfig/xcb-xrm.pc




%changelog

