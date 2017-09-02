Name:		rofi
Version:	1.3.1
Release:	1%{?dist}
Summary:	A window switcher, application launcher, and dmenu replacement

License:	Unknown
URL:		https://github.com/DaveDavenport/rofi
Source0:	https://github.com/DaveDavenport/rofi/releases/download/%{version}/rofi-%{version}.tar.xz

BuildRequires:	libxcb-devel cairo-devel xcb-util-wm-devel xcb-util-devel startup-notification-devel gcc make autoconf automake pango-devel cairo-devel libxcb-devel xorg-x11-util-macros libxkbcommon-devel libxkbcommon-x11-devel xorg-x11-server-devel pkgconfig(xcb-xrm)
Requires:	pango cairo xcb-util xcb-util-wm startup-notification libxcb xorg-x11-server-Xorg pkgconfig(xcb-xrm)

%description


%prep
%setup -q


%build
export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc
%{_bindir}/rofi
%{_bindir}/rofi-sensible-terminal
%{_bindir}/rofi-theme-selector
%{_mandir}/man1/rofi-sensible-terminal.1.gz
%{_mandir}/man1/rofi.1.gz
%{_datarootdir}/rofi/themes/Adapta-Nokto.theme
%{_datarootdir}/rofi/themes/Arc.theme
%{_datarootdir}/rofi/themes/DarkBlue.theme
%{_datarootdir}/rofi/themes/Indego.theme
%{_datarootdir}/rofi/themes/Monokai.theme
%{_datarootdir}/rofi/themes/Paper.theme
%{_datarootdir}/rofi/themes/android_notification.theme
%{_datarootdir}/rofi/themes/blue.theme
%{_datarootdir}/rofi/themes/c64.theme
%{_datarootdir}/rofi/themes/glue_pro_blue.theme
%{_datarootdir}/rofi/themes/gruvbox-dark-hard.theme
%{_datarootdir}/rofi/themes/gruvbox-dark-soft.theme
%{_datarootdir}/rofi/themes/gruvbox-dark.theme
%{_datarootdir}/rofi/themes/gruvbox-light-hard.theme
%{_datarootdir}/rofi/themes/gruvbox-light-soft.theme
%{_datarootdir}/rofi/themes/gruvbox-light.theme
%{_datarootdir}/rofi/themes/lb.theme
%{_datarootdir}/rofi/themes/purple.theme
%{_datarootdir}/rofi/themes/solarized.theme
%{_datarootdir}/rofi/themes/solarized_alternate.theme




%changelog

