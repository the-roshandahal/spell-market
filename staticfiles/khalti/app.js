(() => {
  "use strict";
  var e = {
      334: (e) => {
        var t,
          n = (function (e, t) {
            return (
              (function (e, t) {
                Object.defineProperty(t, "__esModule", { value: !0 });
                var n =
                    "function" == typeof Symbol &&
                    "symbol" == typeof Symbol.iterator
                      ? function (e) {
                          return typeof e;
                        }
                      : function (e) {
                          return e &&
                            "function" == typeof Symbol &&
                            e.constructor === Symbol
                            ? "symbol"
                            : typeof e;
                        },
                  i = (t.SkipValidation = function (e) {
                    (this.name = "SkipValidation"), (this.message = e);
                  }),
                  o = (t.validateSingle = function (e, t, n, o, r) {
                    var a = [];
                    "function" == typeof t && (t = [t]);
                    for (var l = 0; l < t.length; l++)
                      try {
                        var d = t[l](e, o);
                        "string" == typeof d &&
                          a.push(d.replace("{value}", e).replace("{key}", r));
                      } catch (e) {
                        if (e instanceof i) break;
                      }
                    return !0 === n ? a : a.length > 0 ? a[0] : void 0;
                  });
                (t.validate = function (e, t, i) {
                  if (t) {
                    var r = {},
                      a = !0;
                    if (
                      "object" === (void 0 === t ? "undefined" : n(t)) &&
                      !t.length
                    ) {
                      for (var l in t)
                        if (t.hasOwnProperty(l)) {
                          var d = o(e[l], t[l], i, e, l);
                          void 0 !== d && (a = !1), (r[l] = d);
                        }
                      return a ? void 0 : r;
                    }
                    return o(e, t, i);
                  }
                }),
                  (t.required = function (e, t) {
                    function n(e) {
                      return void 0 === e || "" === e || null === e;
                    }
                    return function (o) {
                      if (e && n(o)) return t || "This field is required.";
                      if (!e && n(o)) throw new i();
                    };
                  }),
                  (t.isNumber = function (e) {
                    return function (t) {
                      if ("number" != typeof t || isNaN(t))
                        return e || "'{value}' is not a valid number.";
                    };
                  }),
                  (t.isString = function (e) {
                    return function (t) {
                      if ("string" != typeof t)
                        return e || "'{value}' is not a valid string.";
                    };
                  }),
                  (t.isFunction = function (e) {
                    return function (t) {
                      if ("function" != typeof t)
                        return e || "Expected a function.";
                    };
                  }),
                  (t.isObject = function (e) {
                    return function (t) {
                      if (t !== Object(t)) return e || "Expected an object.";
                    };
                  }),
                  (t.isArray = function (e) {
                    return function (t) {
                      if (
                        "[object Array]" !== Object.prototype.toString.call(t)
                      )
                        return e || "Expected an array.";
                    };
                  }),
                  (t.length = function (e, t) {
                    return function (n) {
                      if ((n + "").length !== e)
                        return t || "It must be " + e + " characters long.";
                    };
                  }),
                  (t.isEmail = function (e) {
                    return function (t) {
                      if (
                        !/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
                          t
                        )
                      )
                        return e || "Invalid email id.";
                    };
                  }),
                  (t.equalsTo = function (e, t) {
                    return function (n, i) {
                      if (n !== i[e])
                        return t || "'{key}' and '" + e + "' do not match.";
                    };
                  }),
                  (t.minLength = function (e, t) {
                    return function (n) {
                      if ((n + "").length < e)
                        return (
                          t || "It must be at least " + e + " characters long."
                        );
                    };
                  }),
                  (t.maxLength = function (e, t) {
                    return function (n) {
                      if ((n + "").length > e)
                        return (
                          t || "It must be at most " + e + " characters long."
                        );
                    };
                  }),
                  (t.isBoolean = function (e) {
                    return function (t) {
                      if (!0 !== t && !1 !== t)
                        return e || "Invalid boolean value.";
                    };
                  }),
                  (t.within = function (e, t) {
                    return function (n) {
                      n instanceof Array || (n = [n]);
                      for (var i = [], o = 0; o < n.length; o++)
                        -1 === e.indexOf(n[o]) && i.push(n[o]);
                      if (i.length > 0)
                        return (
                          t || "[" + i + "] do not fall under the allowed list."
                        );
                    };
                  }),
                  (t.excludes = function (e, t) {
                    return function (n) {
                      n instanceof Array || (n = [n]);
                      for (var i = [], o = 0; o < n.length; o++)
                        -1 !== e.indexOf(n[o]) && i.push(n[o]);
                      if (i.length > 0)
                        return t || "[" + i + "] fall under restricted values.";
                    };
                  }),
                  (t.pattern = function (e, t) {
                    return function (n) {
                      if (!e.test(n))
                        return (
                          t || "'{value}' does not match with the pattern."
                        );
                    };
                  });
              })((t = { exports: {} }), t.exports),
              t.exports
            );
          })();
        (t = n) &&
          t.__esModule &&
          Object.prototype.hasOwnProperty.call(t, "default") &&
          t.default,
          n.SkipValidation,
          n.validateSingle;
        var i = n.validate,
          o = n.required,
          r = (n.isNumber, n.isString, n.isFunction),
          a = n.isObject,
          l = n.isArray,
          d =
            (n.length,
            n.isEmail,
            n.equalsTo,
            n.minLength,
            n.maxLength,
            n.isBoolean,
            n.within,
            n.excludes,
            n.pattern,
            (function () {
              function e(e, t) {
                for (var n = 0; n < t.length; n++) {
                  var i = t[n];
                  (i.enumerable = i.enumerable || !1),
                    (i.configurable = !0),
                    "value" in i && (i.writable = !0),
                    Object.defineProperty(e, i.key, i);
                }
              }
              return function (t, n, i) {
                return n && e(t.prototype, n), i && e(t, i), t;
              };
            })()),
          u = {
            EBANKING: "EBANKING",
            MOBILE_BANKING: "MOBILE_BANKING",
            CONNECT_IPS: "CONNECT_IPS",
            SCT: "SCT",
            KHALTI: "KHALTI",
          },
          s = function (e) {
            return e ? JSON.parse(JSON.stringify(e)) : e;
          },
          c = {
            onSuccess: [o(!0), r()],
            onError: [o(!1), r()],
            onClose: [o(!1), r()],
          },
          f = {
            publicKey: o(!0),
            productUrl: o(!0),
            productIdentity: o(!0),
            productName: o(!0),
            eventHandler: o(!0),
            amount: o(!0),
            merchantData: [o(!1), a()],
            paymentPreference: [o(!1), l()],
          },
          y = (function () {
            function e(t) {
              !(function (e, t) {
                if (!(e instanceof t))
                  throw new TypeError("Cannot call a class as a function");
              })(this, e),
                (this._widgetId = "khalti-widget-" + Date.now()),
                (this._config = t),
                (this._widget = this.attachWidget()),
                this.listenToWidget(),
                (this.paymentType = u),
                (this.widgetLoaded = !1);
            }
            return (
              d(e, [
                {
                  key: "listenToWidget",
                  value: function () {
                    var e = this;
                    window.addEventListener(
                      "message",
                      function (t) {
                        if (t.data.realm)
                          if ("widgetInit" === t.data.realm)
                            e.widgetInit(t.data.payload);
                          else if (
                            "widgetLoad" !== t.data.realm ||
                            e.widgetLoaded
                          ) {
                            if (
                              !t.data.payload ||
                              t.data.payload.widget_id !== e._widgetId
                            )
                              return;
                            var n = "handle_msg_" + t.data.realm;
                            e[n](t.data.payload);
                          } else
                            t.data.payload.loaded &&
                              (e.hideLoader(),
                              e.widgetInit(),
                              (e.widgetLoaded = t.data.payload.loaded));
                      },
                      !1
                    );
                  },
                },
                {
                  key: "msgWidget",
                  value: function (e, t) {
                    ((t = s(t)).widgetId = this._widgetId),
                      (t.source = "checkout_v2.1"),
                      this._widget.contentWindow.postMessage(
                        { realm: e, payload: t },
                        "*"
                      );
                  },
                },
                {
                  key: "handle_msg_widgetInit",
                  value: function () {
                    this.widgetInit();
                  },
                },
                {
                  key: "widgetInit",
                  value: function (e) {
                    var t = s(this._config);
                    delete t.eventHandler, this.msgWidget("paymentInfo", t);
                  },
                },
                {
                  key: "diplayLoader",
                  value: function () {
                    window.document.getElementById(
                      "loader" + this._widgetId
                    ).style.display = "block";
                  },
                },
                {
                  key: "hideLoader",
                  value: function () {
                    window.document.getElementById(
                      "loader" + this._widgetId
                    ).style.display = "none";
                  },
                },
                {
                  key: "validateConfig",
                  value: function () {
                    var e = i(this._config, f);
                    if (e) throw new Error(JSON.stringify(e));
                    var t = i(this._config.eventHandler, c);
                    if (t) throw new Error(JSON.stringify({ eventHandler: t }));
                  },
                },
                {
                  key: "handle_msg_walletPaymentVerification",
                  value: function (e) {
                    this._config.eventHandler.onSuccess(e), this.hide();
                  },
                },
                {
                  key: "handle_msg_widgetError",
                  value: function (e) {
                    var t = this._config.eventHandler.onError;
                    t && t(e);
                  },
                },
                {
                  key: "disableParentScrollbar",
                  value: function () {
                    (this.parentOverflowValue =
                      window.document.body.style.overflowY),
                      (window.document.body.style.overflowY = "hidden");
                  },
                },
                {
                  key: "enableParentScrollbar",
                  value: function () {
                    (window.document.body.style.overflowY =
                      this.parentOverflowValue),
                      (this.parentOverflowValue = null);
                  },
                },
                {
                  key: "show",
                  value: function (e) {
                    Object.assign(this._config, e),
                      this.validateConfig(),
                      this.disableParentScrollbar(),
                      (this._widget.style.display = "block"),
                      this.widgetLoaded
                        ? this.widgetInit()
                        : this.diplayLoader();
                  },
                },
                {
                  key: "handle_msg_hide",
                  value: function () {
                    this.hide();
                    var e = this._config.eventHandler.onClose;
                    e && e();
                  },
                },
                {
                  key: "hide",
                  value: function () {
                    this.enableParentScrollbar(),
                      (this._widget.style.display = "none");
                  },
                },
                {
                  key: "attachWidget",
                  value: function () {
                    var e = window.document.createElement("iframe");
                    e.setAttribute("id", this._widgetId),
                      (e.style.position = "fixed"),
                      (e.style.display = "none"),
                      (e.style.top = "0"),
                      (e.style.left = "0"),
                      (e.width = "100%"),
                      (e.height = window.innerHeight + "px"),
                      e.setAttribute(
                        "src",
                        "https://khalti.s3.ap-south-1.amazonaws.com/KPG/dist/2020.12.22.0.0.0/payment_gateway_widget.html"
                      ),
                      (e.style.zIndex = 99999),
                      e.setAttribute("frameborder", 0),
                      e.setAttribute("allowtransparency", !0);
                    var t = window.document.createElement("div");
                    return (
                      t.setAttribute("id", "loader" + this._widgetId),
                      (t.style.width = "100%"),
                      (t.style.height = "100%"),
                      (t.style.backgroundColor = "rgba(0, 0, 0, 0.5)"),
                      (t.style.top = "0px"),
                      (t.style.left = "0px"),
                      (t.style.position = "absolute"),
                      (t.style.display = "none"),
                      (t.innerHTML =
                        '<img style="position:relative;left:50%;top:50%;transform:translate(-50%, -50%);z-index: 99999;" src=https://khalti.s3.ap-south-1.amazonaws.com/KPG/dist/2020.12.22.0.0.0/icons/infinity-loader.svg></img>'),
                      window.document.body.contains(t) ||
                        window.document.body.appendChild(t),
                      window.document.body.appendChild(e),
                      e
                    );
                  },
                },
              ]),
              e
            );
          })();
        e.exports = y;
      },
    },
    t = {};
  function n(i) {
    var o = t[i];
    if (void 0 !== o) return o.exports;
    var r = (t[i] = { exports: {} });
    return e[i](r, r.exports, n), r.exports;
  }
  (n.n = (e) => {
    var t = e && e.__esModule ? () => e.default : () => e;
    return n.d(t, { a: t }), t;
  }),
    (n.d = (e, t) => {
      for (var i in t)
        n.o(t, i) &&
          !n.o(e, i) &&
          Object.defineProperty(e, i, { enumerable: !0, get: t[i] });
    }),
    (n.o = (e, t) => Object.prototype.hasOwnProperty.call(e, t)),
    (() => {
      var e = n(334);
      let t = {
          publicKey: "test_public_key_c3f2aeb09373408e8510688a7af3ae5e",
          productIdentity: "54s5af45",
          productName: "Fool would buy",
          productUrl: "http://Xina.com.np",
          eventHandler: {
            onSuccess(e) {
              console.log(e);
            },
            onError(e) {
              console.log(e);
            },
          },
          paymentPreference: [
            "MOBILE_BANKING",
            "KHALTI",
            "EBANKING",
            "CONNECT_IPS",
            "SCT",
          ],
        },
        i = new (n.n(e)())(t);
      document
        .getElementById("payment-button")
        .addEventListener("click", () => i.show({ amount: 1e3 }));
    })();
})();
